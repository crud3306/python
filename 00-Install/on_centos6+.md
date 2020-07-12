

Python安装
=========
您需要下载适用于您使用平台的二进制代码，然后安装Python。

如果您平台的二进制代码是不可用的，你需要使用C编译器手动编译源代码。
编译的源代码，功能上有更多的选择性， 为python安装提供了更多的灵活性。



Python最新源码，二进制文档，新闻资讯等可以在Python的官网查看到：  
Python官网：https://www.python.org/

你可以在以下链接中下载 Python 的文档，你可以下载 HTML、PDF 和 PostScript 等格式的文档。  
Python文档下载地址：https://www.python.org/doc/


安装
----------

安装相应的编译工具
```sh
#yum groupinstall 'Development Tools'
#Development 套件里面安装的工具较多，包括 git 等
yum install -y gcc gcc-c++ openssl openssl-devel ncurese-devel zlib zlib-devel bzip2-devel pcre pcre-devel libffi-devel zlib1g-dev
```

下载、解压、编译 安装
```sh
#下载 Download Gzipped source tarball
wget https://www.python.org/ftp/python/3.6.11/Python-3.6.11.tgz

#建立一个空文件夹，用于存放python3程序
mkdir /usr/local/python3

#解压
tar -zxvf Python-3.6.11.tgz

#执行配置文件，编译，编译安装
cd Python-3.6.11 
./configure --prefix=/usr/local/python3 --enable-optimizations --with-ssl
#第一个，指定安装的路径,不指定的话,安装过程中可能软件所需要的文件复制到其他不同目录,删除软件很不方便,复制软件也不方便.
#第二个，可以提高python10%-20%代码运行速度.
#第三个，如果 python3以上版本须指定，是为了安装pip需要用到ssl,后面报错会有提到。

make && make install
#python的 make install过程较慢，耐心等待吧。
#一些依赖提前装好，以免make报错后，又再make，浪费太多时间。
```


配置
----------

直接建软链
```sh
ll /usr/bin |grep python

ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

#或者软链至/usr/local/bin/下
#ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
#ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3
```

或者 用下面的方式，前提是系统中无安装其它版本的python，否则会冲突
```sh
#设置环境变量
vi ~/.profile
export PYTHONPATH=/usr/local/python3   #（你解压后的目录，即安装目录）
export PATH=$PYTHONPATH/bin:$PATH

#刷新环境变量
source ~/.profile
```


检查正常可用：
----------
```sh
#python -V
python3 -V

#输出版本号，则安装成功
Python 3.6.11
```


如果/usr/local/python3/bin/没有pip、pip3.7，则需要：
--------
下载pip：wget  https://bootstrap.pypa.io/get-pip.py  
安装：python3 get-pip.py   
升级：pip3 install --upgrade pip  




参考地址：  
----------
https://www.cnblogs.com/xiujin/p/11477419.html




安装时问题
==========

zipimport.ZipImportError: can't decompress data; zlib not available
----------
从错误信息分析，就是缺少了zlib的解压缩类库，安装即可
> yum -y install zlib*

安装完成之后，重新make


ModuleNotFoundError: No module named 'ctypes'
----------
需要安装依赖
> yum -y install libffi-devel 







安装pipenv
-----------
在centos中使用python3.7或以上版本,进行pip install 命令容易报错
```sh
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https:*******: There was a problem confirming the ssl certificate: 
Can't connect to HTTPS URL because the SSL module is not available. - skipping
```
在./configure过程中，如果没有加上–with-ssl参数时，默认安装的软件涉及到ssl的功能不可用，刚好pip3过程需要ssl模块，而由于没有指定，所以该功能不可用。解决办法是重新对python3.6进行编译安装，用一下过程来实现编译安装:
```sh
cd Python-3.7.2
./configure --prefix=/usr/local/python3 --enable-optimizations --with-ssl
make && make install
```
即可正常使用pip安装。



修改pip安装源
-----------
修改系统pip安装源
在家目录下新建.pip文件夹,进入文件夹新建文件pip.conf之后写入相应镜像网站地址
```sh
cd ~
mkdir .pip
cd .pip
vim pip.conf

#进入后添加以下内容,保存退出.
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
```


修改pipenv安装源
-----------
在自己的虚拟环境中找到Pipfile文件,将其中的url = "https://pypi.org/simple"，  
修改为你需要的国内镜像,如https://mirrors.aliyun.com/pypi/simple/
```sh
[root@localhost myproject]# vim Pipfile 

#进入后添加以下内容,保存退出.
[[source]]
name = "pypi"
url = "https://pypi.org/simple" # 改为url = "https://mirrors.aliyun.com/pypi/simple/"
verify_ssl = true

[dev-packages] #这里是开发环境专属包,使用pipenv install --dev package来安装专属开发环境的包

[packages] # 全部环境的通用包,安装在这里.

[requires]
python_version = "3.7"
```

