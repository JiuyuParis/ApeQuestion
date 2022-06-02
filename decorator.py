from functools import wraps

from flask import g, redirect, url_for

# 登录装饰器
def require_login(func):
    # 加上这个注解不会丢失参数
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,'user'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('user.login'))
    return wrapper