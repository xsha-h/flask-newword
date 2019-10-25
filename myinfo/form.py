from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class UserForm(FlaskForm):
    user_email = StringField(label="邮箱", validators=[DataRequired(), Email()])
    user_name = StringField(label="昵称", validators=[DataRequired(), Length(3, 18)])
    old_password = PasswordField(label="新密码", validators=[DataRequired(), Length(3, 18)])
    new_password = PasswordField(label="再次确认新密码", validators=[DataRequired(), Length(3, 18), EqualTo(old_password)])
    user_introduction = TextAreaField(label="简介")
    avatar_btn = FileField(validators=[FileAllowed(["jpg", "png", "gif"])])
    submit_btn = SubmitField("保存")
