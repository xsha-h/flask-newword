from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    user_name = StringField(label="用户名", validators=[DataRequired(), Length(3, 18)])
    user_psd = PasswordField(label="密码", validators=[DataRequired(), Length(3, 18)])
    remember_btn = BooleanField(label="记住密码")
    login_btn = SubmitField("登录")
