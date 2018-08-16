# -*- coding: utf-8 -*-
from app import app
#from flask import Flask

__author__ = "qianm"

#app = create_app()
#app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'hello world'

@app.before_request
def process_request1(*args, **kwargs):
	print('我app来了1')
	#return '1234'

@app.before_request
def process_request2(*args, **kwargs):
	print('我app来了2')


if __name__ == '__main__':
	# 如果要使用vscode调试，需要将debug设置为False，否则无法命中请求断点
    app.run(host='0.0.0.0', debug=True)