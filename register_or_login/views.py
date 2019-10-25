from flask import Blueprint, render_template, request, redirect, url_for, session

from models import User, db
from register_or_login.forms import RegisterForm, LoginForm

reg_or_log_bp = Blueprint("reg_or_log", __name__)


@reg_or_log_bp.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("register.html", form=form)

    if form.validate_on_submit():
        try:
            user = User()
            user.user_name = request.form.get("user_name")
            user.user_email = request.form.get("user_email")
            user.user_psd = request.form.get("user_psd")
            # 默认权限状态为0
            user.user_state = 0
            user.user_active = 1

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("reg_or_log.login_page"))
        except Exception as e:
            print(e)
            db.session.rollback()
    return render_template("register.html", form=form)


@reg_or_log_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        if form.validate_on_submit():
            user = User.query.filter(User.user_active == 1,
                                     User.user_name == request.form.get("user_name"),
                                     User.user_psd == request.form.get("user_psd")).first()

            if user:
                # 设置session值
                session["user_name"] = request.form.get("user_name")
                session["user_psd"] = request.form.get("user_psd")

                return redirect(url_for("index_page"))
        return render_template("login.html", form=form)


@reg_or_log_bp.route("/logout")
def logout_page():
    # 删除session值
    session.clear()
    return redirect(url_for("reg_or_log.login_page"))
