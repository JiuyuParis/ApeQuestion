import random
import string
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from flask_mail import Message

from form import RegisterForm, LoginForm
from model import RegisterCapture, User
from extension import mail, db
from werkzeug import security

bp = Blueprint(name="user", import_name=__name__, url_prefix='/user/')

# 登录功能
@bp.route('/login',methods=['get','post'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        login_form=LoginForm(request.form)
        if login_form.validate():
            user=User.query.filter_by(email=login_form.email.data).first()
            # 如果用户存在且密码正确
            if user and security.check_password_hash(user.password,login_form.password.data):
                session['user_id']=user.id
                return redirect('/')
            else:
                # 反射一条消息到下一个请求，人话就是渲染模板时附带一条消息
                flash("邮箱或密码错误")
                return render_template('login.html',email=request.form.get("email"),password=request.form.get("password"))
        else:
            flash("邮箱或密码格式错误")
            return render_template('login.html',email=request.form.get("email"),password=request.form.get("password"))

# 用户注册功能
@bp.route('/register',methods=['get','post'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        register_form=RegisterForm(request.form)
        if register_form.validate():# 注册校验成功，添加用户到数据库
            # 密码加密
            password_hash=security.generate_password_hash(register_form.password.data)
            user=User(email=register_form.email.data,username=register_form.username.data,password=password_hash)
            db.session.add(user)
            db.session.commit()
            # 重定向到登录页面
            return redirect(url_for('user.login'))
        else:
            # 校验错误字典
            data={}
            # 数据回显
            data.update(emailP=request.form.get("email"),usernameP=request.form.get("username"),captureP=request.form.get("capture"),
                        passwordP=request.form.get("password"),password_confirmP=request.form.get("password_confirm"))
            # 将校验信息由列表转换为字符串
            for key in register_form.errors.keys():
                data[key]=' '.join(register_form.errors[key])
                # 为什么无法改变register_form.errors字典
                register_form.errors[key]=''.join(register_form.errors[key])
            print(register_form.errors)
            return render_template('register.html',**data)

# 发送邮箱验证码
@bp.route('/capture')
def get_capture():
    # 验证码字符库，英文大小写+数字
    characters = string.ascii_letters + string.digits
    # 验证码
    capture = ''.join(random.sample(characters, 4))
    # 邮箱
    email = request.args.get("email")
    if email:
        message = Message(subject="【猿问答】注册验证码", recipients=[email], body=f'您的注册验证码为【{capture}】,请勿泄露')
        mail.send(message)
        # 在数据库中register_capture表中查找该邮箱数据 查找为空的话返回空列表而非None
        register_capture = RegisterCapture.query.filter_by(email=email).first()
        if register_capture:  # 如果数据库中有这个邮箱，那么就更新验证码
            register_capture.capture = capture
            register_capture.create_time = datetime.now()
            db.session.commit()
        else:  # 如果没有则添加一条数据
            register_capture = RegisterCapture(email=email, capture=capture)
            db.session.add(register_capture)
            db.session.commit()
        return jsonify({"code":200,"message":"发送成功"})
    else:
        return jsonify({"code":500,"message":"请输入邮箱"})

@bp.route('/logout')
def logout():
    # 清除session
    session.clear()
    return redirect(url_for('user.login'))