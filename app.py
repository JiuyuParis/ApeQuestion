from flask import Flask, session, g
from flask_migrate import Migrate

import config
from extension import db, mail
from model import User
from modules import user_bp
from modules import question_bp

app = Flask(__name__)

# 项目配置
app.config.from_object(config)
# db绑定到app
db.init_app(app)
# mai绑定到app
mail.init_app(app)
# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)
# 使用Flask-Migrate
migrate = Migrate(app=app, db=db)


# 钩子函数，请求之前执行
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:# 如果session中有user_id
        user = User.query.get(user_id)
        g.user = user

# 上下文处理器，渲染模板时执行
@app.context_processor
def context_processor():
    if hasattr(g,'user'):
        return {'user':g.user}
    else:
        return {}

if __name__ == '__main__':
    app.run()
