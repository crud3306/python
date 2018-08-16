# -*- coding: utf-8 -*-
from flask import Flask

__author = 'qianm'

def register_web_blueprint(app):
    from app.web import web
    from app.api.v1 import api as api_v1
    from app.api.v2 import api as api_v2
    #注册蓝图，同时可指定一个统一前缀
    app.register_blueprint(web)
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(api_v2, url_prefix='/api/v2')

#实例化Flask
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')
app.config.from_object('app.config.secure')
app.config.from_object('app.config.settings')

#注册蓝图
register_web_blueprint(app)

#def create_app():
#	app = Flask(__name__)
#	app.config.from_object('app.config.secure')
#	app.config.from_object('app.config.settings')
    
#    return app

    # register_web_blueprint(app)