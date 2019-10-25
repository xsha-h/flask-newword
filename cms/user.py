from flask import Blueprint, render_template, request
from flask_login import login_required
from sqlalchemy import or_

from models import User, db

cms_user_bp = Blueprint("cms_user", __name__)


# 自定义过滤器(激活/冻结)
@cms_user_bp.app_template_filter("bool_to_str")
def bool_to_str(value, active, negative):
    return active if value else negative


# 自定义过滤器(设置默认值)
@cms_user_bp.app_template_filter("set_default")
def set_default(value):
    return value if value else "未填写"


@cms_user_bp.route("/user", methods=["GET", "POST"])
@cms_user_bp.route("/user/<int:page>", methods=["GET", "POST"])
@login_required
def cms_user(page=1):
    """
    装饰器@login_required会自动检测这次请求的页面有没有session值
    :param page:  获取当前的页面的页数
    :return:
    """
    if request.method == "GET":
        users = User.query.paginate(page=page, per_page=10)

    else:
        keyword = request.form.get("keyword")
        if keyword != "1" and keyword == "活跃":
            users = User.query.filter(User.user_active == 1).paginate(page=page, per_page=10)
        elif keyword != "0" and keyword == "冻结":
            users = User.query.filter(User.user_active == 0).paginate(page=page, per_page=10)
        else:
            users = User.query.filter(or_(User.user_name.like("%"+keyword+"%"), User.user_email.like("%"+keyword+"%"),
                                          User.user_phone.like("%"+keyword+"%"))).paginate(page=page, per_page=10)

    return render_template("cms/user.html", users=users.items, pagination=users)


@cms_user_bp.route("/user/active", methods=["GET", "POST"])
def set_active():

    """
    修改用户的状态
    :return: 返回0或者1
    """
    user_id = request.form.get("user_id")
    user = User.query.get(user_id)
    # 冻结用户
    if user.user_active:
        try:
            user.user_active = 0
            db.session.commit()
            return "0"
        except Exception as e:
            print(e)
            db.session.rollback()
            return "1"
    # 激活用户
    else:
        try:
            user.user_active = 1
            db.session.commit()
            return "1"
        except Exception as e:
            print(e)
            db.session.rollback()
            return "0"


@cms_user_bp.route("/user/check", methods=["GET", "POST"])
def check_user():

    """
    产看用户的相关信息
    :return: 返回当前用户信息字典（json格式字符串）
    """

    user = User.query.get(request.form.get("user_id"))
    return {
        "user_name": user.user_name,
        "user_phone": user.user_phone or "未填写",
        "user_email": user.user_email,
        "create_time": "/".join([str(user.create_time.year), str(user.create_time.month), str(user.create_time.day)]),
        "user_active": "活跃" if user.user_active else "冻结",
        "user_avatar": "/static/media/"+user.user_avatar if user.user_avatar else "/static/media/avatar.png",
        "user_introduce": user.user_introduce
    }


@cms_user_bp.route("/user/reset", methods=["GET", "POST"])
def reset_password():

    """
    重置密码
    :return: 空字符串
    """

    user = User.query.get(request.form.get("user_id"))
    # 自定义默认密码是123456+用户名
    user.user_psd = "123456"+user.user_name
    db.session.commit()
    return ""
