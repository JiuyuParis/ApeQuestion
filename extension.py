# 扩展模块
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# 创建SQLAlchemy实例对象
db=SQLAlchemy()
# 实例化邮箱对象
mail=Mail()