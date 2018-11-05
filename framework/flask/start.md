
安装
========================
pip install flask

基本使用
========================
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'hello world'

if __name__ == '__main__':
	app.run()
	#app.run(debug=True, port=8000, host='0.0.0.0')


用蓝图 Blueprint
========================
蓝图用于拆分多视图目录或多app目录，不用所有route均写在一起

先在一个文件中使用蓝图
xxx1.py
from flask import Blueprint

blue_xxx1 = Blueprint('xxx1', __name__)

然后，在app上注册蓝图
from xxx1 import blue_xxx1

app = Flask(__name__)
app.register_blueprint(blue_xxx1, url_prefix="/随便指定个前缀；如果不用，则不加该参数")


请求扩展，可用于 在请求前验证接口权限
========================
@app.before_first_request
@app.before_request
@app.after_request

针对app来写，则所有请求都生会生效
也可针对蓝图来写，此时只针对某蓝图生效
@blue_xxx1.before_request
...


例：
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'hello world'

@app.before_request
def process_request(*args **kwargs):
	print('我来了')

if __name__ == '__main__':
	app.run()



可写多个
--------------------
@app.before_request
def process_request1(*args, **kwargs):
	print('我来了1')

@app.before_request
def process_request2(*args, **kwargs):
	print('我来了2')

@app.before_first_request
def first_request1(*args, **kwargs):
	print('我first来了1')

@app.before_first_request
def first_request2(*args, **kwargs):
	print('我first来了2')

@app.after_request
def after_request1(*args, **kwargs):
	print('我闪了1')

@app.after_request
def after_request2(*args, **kwargs):
	print('我闪了2')




表单验证
========================





DBUtils
========================

两种安装方式：


第一种：下载源码，来安装
------------------------
打开地址： https://pypi.python.org/pypi/DBUtils/1.2
先下载你要安装的包，并解压到磁盘下；
进入到该文件的setup.py 目录下 ，打开cmd，并切换到该目录下；
先执行 python setup.py build
然后执行 python setup.py install

第二种：直接安装
------------------------
pip install DBUtils
或指定版本
pip install DBUtils==1.2



使用：







