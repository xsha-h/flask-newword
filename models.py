from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime

from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True)
    add_time = db.Column(db.Date, default=datetime.date.today())
    words = db.relationship("Word", backref="groups")


class Word(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False, unique=True)
    translation = db.Column(db.String(30), nullable=False)
    introduction = db.Column(db.String(100), default="")
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id", ondelete="RESTRICT"), nullable=False)
    add_time = db.Column(db.Date, default=datetime.date.today())
    star = db.Column(db.Integer, default=0)
    example = db.Column(db.String(150), nullable=False)
    tag = db.Column(db.Integer, default=0)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    user_psd = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    user_phone = db.Column(db.String(11))
    user_active = db.Column(db.Integer)
    user_avatar = db.Column(db.String(100))
    user_introduce = db.Column(db.String(100))
    user_state = db.Column(db.Integer, nullable=False, default=0)
    user_recv = db.Column(db.Integer)

    feedbacks = db.relationship("Feedback", backref="users")

    # 给密码加密
    def set_password(self, password):
        self.user_psd = generate_password_hash(password)

    # 验证密码
    def check_password(self, password):
        return check_password_hash(self.user_psd, password)


class Feedback(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)
    add_time = db.Column(db.DateTime, default=datetime.datetime.now())
    content = db.Column(db.String(100), nullable=False)
    is_checked = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class Composition(db.Model):
    __tablename__ = "compositions"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    content = db.Column(db.Text, nullable=False)
