from flask import Blueprint, render_template, request, flash, g, url_for, redirect
from sqlalchemy import or_

from decorator import require_login
from extension import db
from form import QuestionForm, AnswerForm
from model import Question, Answer

bp=Blueprint(name="question",import_name=__name__,url_prefix='/')

@bp.route('/')
def index():
    # 查询问题列表
    question_list=Question.query.order_by(db.text('-public_time')).all()
    return render_template('index.html',question_list=question_list)

# 发布问答
@bp.route('/question/public',methods=['get','post'])
@require_login # 该注解相当于将函数作为参数传进去，即require_login(public_question)，最终执行的是wrapper(*args,**kwargs)
def public_question():
    if request.method=='GET':
        return render_template('question.html')
    else:
        question_form=QuestionForm(request.form)
        if question_form.validate():
            question=Question(title=question_form.title.data,content=question_form.content.data,user=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('question.index',public=True))
        else:
            flash('请检查是否输入标题和内容，内容不能少于5个字符')
            return render_template('question.html',title=request.form.get("title"),content=request.form.get('content'))

# 发布问题
@bp.route('/question/detail/<int:question_id>')
def question_detail(question_id):
    # 根据id查询问题
    question=Question.query.get(question_id)
    return render_template('detail.html',question=question)

# 评论回复
@bp.route('/question/answer/<int:question_id>',methods=['post'])
@require_login
def comment(question_id):
    answer_form=AnswerForm(request.form)
    if answer_form.validate():
        answer=Answer(content=answer_form.content.data,question_id=question_id,user=g.user)
        db.session.add(answer)
        db.session.commit()
    else:
        flash("内容不能为空")
    return redirect(url_for('question.question_detail',question_id=question_id))

@bp.route('/question/search')
def search():
    kw=request.args.get('keyword')
    questions=Question.query.filter(or_(Question.title.contains(kw),Question.content.contains(kw))).order_by(db.text('-public_time'))
    return render_template('index.html',question_list=questions)