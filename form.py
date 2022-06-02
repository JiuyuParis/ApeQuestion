import wtforms
from wtforms import SubmitField
from wtforms.validators import email, InputRequired, length, EqualTo

from model import RegisterCapture, User


# 注册表单验证类
class RegisterForm(wtforms.Form):
    email=wtforms.StringField(validators=[email(message='输入的邮箱有误')])
    username=wtforms.StringField(validators=[InputRequired(message='请输入用户名')])
    capture=wtforms.StringField(validators=[length(min=4,max=4,message='')])
    password=wtforms.StringField(validators=[length(min=6,max=20,message='密码长度在6-20位之间')])
    password_confirm=wtforms.StringField(validators=[EqualTo('password',message='两次输入密码不一致')])

    # 校验验证码是否正确
    def validate_capture(self,field):
        register_capture=RegisterCapture.query.filter_by(email=self.email.data).first()
        # 如果没有发送验证码到邮箱或验证码不匹配
        if not register_capture or field.data.lower()!=register_capture.capture.lower():
            raise wtforms.ValidationError('验证码错误')

    # 查看邮箱是否已经注册
    def validate_email(self,field):
        register_capture=User.query.filter_by(email=field.data).first()
        if register_capture:
            raise wtforms.ValidationError('邮箱已经注册')

# 登录表单验证类
class LoginForm(wtforms.Form):
    email=wtforms.StringField(validators=[email(message='是否输入了邮箱')])
    password=wtforms.StringField(validators=[length(min=6,max=20)])

# 发布问题表单验证
class QuestionForm(wtforms.Form):
    title=wtforms.StringField(validators=[InputRequired(message='是否输入标题')])
    content=wtforms.StringField(validators=[length(min=5)])

# 评论回复表单验证
class AnswerForm(wtforms.Form):
    content=wtforms.StringField(validators=[InputRequired()])