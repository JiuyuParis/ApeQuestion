from datetime import datetime

from extension import db

# 注册验证码实体类
class RegisterCapture(db.Model):
    __name__="register_capture"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(200),nullable=False,unique=True)
    capture=db.Column(db.String(10),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)

# 用户实体类
class User(db.Model):
    __name__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(200),nullable=False,unique=True)
    username=db.Column(db.String(200),nullable=False,unique=True)
    password=db.Column(db.String(200),nullable=False)
    join_time=db.Column(db.DateTime,default=datetime.now)

# 问题实体类
class Question(db.Model):
    __name__="question"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(200),nullable=False)
    content=db.Column(db.Text,nullable=False)
    public_time=db.Column(db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    user=db.relationship('User',backref='questions')

# 评论回复实体类
class Answer(db.Model):
    __name__='answer'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.Text,nullable=False)
    answer_time=db.Column(db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    question_id=db.Column(db.Integer,db.ForeignKey('question.id'))

    user=db.relationship('User',backref='answers')
    question=db.relationship('Question',backref=db.backref('answers',order_by=answer_time.desc()))