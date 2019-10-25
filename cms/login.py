from flask import Blueprint, render_template, views, redirect, url_for, flash
from flask_login import LoginManager, login_required

from cms.forms import LoginForm
from models import User
from flask_login import login_user, logout_user


# 指定没有登录时重定向的页面
login_manager = LoginManager()
login_manager.login_view = "cms_login.cms_login"
cms_login_bp = Blueprint("cms_login", __name__)


# 采用了基于调度方法的类视图
class CMSLogin(views.MethodView):
    """
    get方法是对应前台的get请求
    post方法是对应前台的post请求
    """
    def get(self):
        login_form = LoginForm()
        return render_template("cms/login.html", form=login_form)

    def post(self):
        login_form = LoginForm()
        user_name = login_form.user_name.data
        user_psd = login_form.user_psd.data
        user = User.query.filter(User.user_name == user_name,
                                 User.user_psd == user_psd).first()
        if user:
            if user.user_state:

                # 自动生成一个session
                login_user(user)
                return redirect(url_for("cms_user.cms_user"))
            else:
                # 向后台登录页面闪现一条消息
                flash("您还未有管理员权限！")
                return render_template("cms/login.html", form=login_form)
        else:
            flash("账号或密码错误，请重新输入！")
            return render_template("cms/login.html", form=login_form)


# 用add_url_rule()注册路由
cms_login_bp.add_url_rule("/login",  view_func=CMSLogin.as_view("cms_login"))


@cms_login_bp.route("/logout")
@login_required
def logout():
    login_form = LoginForm()

    # 自动删除session
    logout_user()
    return render_template("cms/login.html", form=login_form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
