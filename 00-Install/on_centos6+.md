


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
```sh
#下载 Download Gzipped source tarball
wget https://www.python.org/ftp/python/3.6.11/Python-3.6.11.tgz

#编压，编译安装
tar -zxvf Python-3.6.11.tgz -C /usr/local
ln -s Python-3.6.11 python3
cd python3
./configure
make && make install
```


配置
----------
```sh
#设置环境变量
vi ~/.profile
export PYTHONPATH=/usr/local/python3   #（你解压后的目录，即安装目录）
export PATH=$PYTHONPATH/bin:$PATH

#刷新环境变量
source ~/.profile
```

或者直接建软链
```sh
ll /usr/bin |grep python
ln -s /usr/local/python3/bin/python /usr/bin/python3
```



检查正常可用：
----------
```sh
#python -V
python3 -V
Python 3.6.11
```

