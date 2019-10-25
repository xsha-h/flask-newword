from flask import Blueprint, render_template, request, url_for, session, abort
from werkzeug.utils import secure_filename, redirect
import os
import re

from helper import check_user
from models import User, db

# 获取存储图片的路径
UPLOAD_PATH = os.path.join("static/media")

myinfo_bp = Blueprint("myinfo", __name__)


# 自定义过滤器
@myinfo_bp.app_template_filter("email_filter")
def email_filter(email):
    arr = email.split("@")
    return email[:3]+"*****@"+arr[1]


@myinfo_bp.route("/", methods=["GET", "POST"])
def myinfo_page():

    if not check_user():
        # abort(404)
        return redirect(url_for("reg_or_log.login_page"))
    else:
        if request.method == "GET":
            user = User.query.filter(User.user_name == session.get("user_name"),
                                     User.user_psd == session.get("user_psd")).first()

            # 自定义密码显示难度的正则表达式
            pattern = re.compile(r"[a-zA-Z]")
            res = pattern.findall(user.user_psd)
            if len(user.user_psd) < 10:
                rank = "低"
            elif len(user.user_psd) < 12 and len(res) < 6:
                rank = "中"
            else:
                rank = "高"

            return render_template("myinfo.html", user=user, rank=rank)
        else:
            try:
                user = User.query.filter(User.user_name == session.get("user_name"),
                                         User.user_psd == session.get("user_psd")).first()
                user.user_name = request.form.get("user_name")
                user.user_phone = request.form.get("user_phone")
                user.user_introduce = request.form.get("user_introduce")
                # 获取文件上传的信息
                avatar_file = request.files.get("avatar_file")
                # 组织成一个标准的文件路径，如果标准文件为空，就不保存文件
                temp_file = secure_filename(avatar_file.filename)

                if temp_file:
                    user.user_avatar = temp_file
                if "jpg" in temp_file or "png" in temp_file or "gif" in temp_file:
                    avatar_file.save(os.path.join(UPLOAD_PATH, user.user_avatar))
                    db.session.commit()

            except Exception as e:
                print(e)
                db.session.rollback()
            return render_template("myinfo.html", user=user)


# 设置密码
@myinfo_bp.route("/set_password", methods=["GET", "POST"])
def set_password():
    if request.method == "GET":
        return redirect(url_for("myinfo.myinfo_page"))
    else:
        user_psd = request.form.get("user_psd")
        again_psd = request.form.get("again_psd")
        if 5 < len(user_psd) < 18 and user_psd == again_psd:
            try:
                user = User.query.filter(User.user_name == session.get("user_name"),
                                         User.user_psd == session.get("user_psd")).first()
                user.user_psd = user_psd
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            return redirect(url_for("myinfo.myinfo_page"))


# 设置邮箱
@myinfo_bp.route("/set_email", methods=["GET", "POST"])
def set_email():
    try:
        user = User.query.filter(User.user_name == session.get("user_name"),
                                 User.user_psd == session.get("user_psd")).first()

        user.user_email = request.form.get("user_email")
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for("myinfo.myinfo_page"))


# 消息通知的接受与否
@myinfo_bp.route("/set_recv", methods=["GET", "POST"])
def set_recv():
    recv = request.form.get("user_recv")
    user = User.query.filter(User.user_name == session.get("user_name"),
                             User.user_psd == session.get("user_psd")).first()

    user.user_recv = int(recv)
    if user.user_recv == 1:
        try:
            db.session.commit()
            res = "消息接收已开启！"
        except Exception as e:
            print(e)
            db.session.rollback()
            res = "消息切换失败"
        return res
    else:
        try:
            db.session.commit()
            res = "消息接收已关闭！"
        except Exception as e:
            print(e)
            db.session.rollback()
            res = "消息切换失败"
        return res


