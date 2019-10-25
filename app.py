import datetime

from flask import Flask, render_template

from helper import check_user
from models import db, Group, Composition

from index.views import index_bp
from word.views import word_bp
from group.views import group_bp
from myinfo.views import myinfo_bp
from feedback.views import feedback_bp
from about.views import about_bp
from register_or_login.views import reg_or_log_bp

from cms.login import cms_login_bp, login_manager
from cms.user import cms_user_bp
from cms.feedback import cms_feedback_bp

app = Flask(__name__)
app.register_blueprint(index_bp, url_prefix="/index")
app.register_blueprint(word_bp, url_prefix="/word")
app.register_blueprint(group_bp, url_prefix="/group")
app.register_blueprint(myinfo_bp, url_prefix="/myinfo")
app.register_blueprint(feedback_bp, url_prefix="/feedback")
app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(reg_or_log_bp)

app.register_blueprint(cms_login_bp, url_prefix="/cms")
app.register_blueprint(cms_user_bp, url_prefix="/cms")
app.register_blueprint(cms_feedback_bp, url_prefix="/cms")


# 配置变量
app.config["SECRET_KEY"] = "this is a 'newword' app"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/newword"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config.from_object("settings")
app.app_context().push()
db.init_app(app)
login_manager.init_app(app)


@app.route('/')
def index_page():
    """
    获取当天是周几，每天的文章都需要不一样
    :return:
    """
    today = datetime.datetime.now().weekday()
    groups = Group.query.limit(5).all()
    composition = Composition.query.get(today+1)

    return render_template("index.html", composition=composition, groups=groups)


# 模板的全局变量
@app.template_global("login")
def global_val():
    """
    定义模板的全局变量，在模板中使用login()即可
    验证用户是否登录
    :return:在模板显示"登录 or "注销"
    """
    login = "注销"
    if not check_user():
        login = "登录"
    return login


@app.template_global("username")
def global_username():
    """
    定义模板的全局变量，在模板中使用username()即可
    验证用户是否登录
    :return: 在模板上显示"用户名" or "请登录"
    """
    if not check_user():
        username = "请登录"
    else:
        username = check_user().user_name
    return username


@app.template_global("avatar")
def global_avatar():
    """
    定义模板的全局变量，在模板中使用avatar()即可
    验证用户是否登录
    :return: 在模板上显示"用户的头像" or "默认头像"
    """
    if not check_user():
        avatar = "没有头像"
    else:
        avatar = check_user().user_avatar
    return avatar


# @app.errorhandler(404)
# def page_not_fount(error):
#     return render_template("page_not_found.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
