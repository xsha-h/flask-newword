from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


# 前台注册表单验证
class RegisterForm(FlaskForm):
    user_name = StringField(label="用户名", validators=[DataRequired(), Length(3, 18)])
    user_email = StringField(label="邮箱", validators=[DataRequired(), Email()])
    user_psd = PasswordField(label="密码", validators=[DataRequired(), Length(3, 18)])
    again_psd = PasswordField(label="确认密码", validators=[EqualTo("user_psd")])
    check_code = IntegerField(label="验证码")
    register_btn = SubmitField("注册")

    def validate_check_code(self, field):
        if field.data < 1000 or field.data > 9999:
            raise ValidationError("验证码错误")


# 后台登陆表单验证
class LoginForm(FlaskForm):
    user_name = StringField(label="用户名", validators=[DataRequired(), Length(3, 18)])
    user_psd = PasswordField(label="密码", validators=[DataRequired(), Length(3, 18)])
    remember_btn = BooleanField(label="记住密码")
    login_btn = SubmitField("登录")
