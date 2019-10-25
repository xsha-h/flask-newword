from flask import session

from models import User


# 检验登录的用户
def check_user():
    user_name = session.get("user_name")
    user_psd = session.get("user_psd")
    user = User.query.filter(User.user_name == user_name,
                             User.user_psd == user_psd).first()

    return user
