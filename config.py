# 项目配置文件

from urllib.parse import quote_plus as urlquote
# 连接MySQL参数
HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='ape_question'
USERNAME='root'
PASSWORD='paris2030@ROOT'
# 注意：如果密码中有特殊符@，那么要quote一下密码，使url对特殊符号进行编码
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,urlquote(PASSWORD),HOSTNAME,PORT,DATABASE)
# 配置连接数据库
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=True

# session密钥
SECRET_KEY='apequestion'

# Flask-Mail配置邮箱
MAIL_SERVER ='smtp.163.com'
MAIL_PORT ='465'
MAIL_USE_TLS =False
MAIL_USE_SSL =True
MAIL_DEBUG =True
# 一下替换成自己的
# 邮箱地址
MAIL_USERNAME ='liuchangxingparis@163.com'
# 授权码
MAIL_PASSWORD ='OKLIWEYYWGWIYAXO'
# 默认发送者
MAIL_DEFAULT_SENDER ='liuchangxingparis@163.com'