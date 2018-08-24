参考地址：
----------
https://docs.scrapy.org/en/latest/
https://docs.scrapy.org/en/latest/topics/commands.html （命令行命令）


安装
----------
> pip3 install scrapy
验证是否安装成功，直接在命令行执行scrapy，看是否有信息输出。
> scrapy


练习抓取地址
----------
> http://quotes.toscrape.com


创建爬虫项目
----------
> scrapy startproject 项目名  
> cd 项目名  
可以看到scrapy.cfg 和 一个与项目同名的目录  
  
  
  
创建spider
----------
> scrapy genspider spider名称 要爬的目标域名(不带http协议)
例：  
> scrapy genspider quotes quotes.toscrape.com   
在spiders目录下生成了一个名为：你指定的spider名称.py 的文件，比如这里是quotes.py  
  
  
生成指定模板的spider
----------
> scrapy genspider -t 模板名 spider名称 要爬的目标域名(不带http协议)  
  
模板有哪些，可以通过下面命令查看  
> scrapy genspider -l  


更改spider代码：
class ...
     ...
     def parse(self, response):
          fname = response.url.split(‘/‘)[-1]
          with open(name, ‘wb’) as f:
               f.write(response.body)
          self.log(‘saved file %s.’, % name)
          pass



执行spider
----------
> scrapy crawl spider名称  
例：  
执行只输出过程与统计结果，但不保存  
> scrapy crawl quotes  
  
执行，并保存结果  
> scrapy crawl quotes -o quotes.json    
> scrapy crawl quotes -o quotes.csv  
> scrapy crawl quotes -o quotes.xml  
> scrapy crawl quotes -o quotes.jl  
注意：  
-o 参数，后面通过文件后缀，自动存为各种数据格式的文件。  
  
直接执行，并存到指定的ftp服务器上  
> scrapy crawl quotes -o ftp://user:pass@ftp.example.com/pathxxx/quotes.csv  
  
  
检测代码是否有误  
-----------
> scrapy check  
  
  
列出项目中所有spider名称  
-----------
> scrapy list  


抓取指定网页
-----------
> scrapy fetch [options] <url>  
option:  
--spider=SPIDER: bypass spider autodetection and force use of specific spider  
—nolog：只显示内容不要执行过程的log  
--headers: print the response’s HTTP headers instead of the response’s body  
--no-redirect: do not follow HTTP 3xx redirects (default is to follow them)  
  
例：  
> scrapy fetch --nolog http://www.example.com/some/page.html  
> [ ... html content here ... ]  
  
> scrapy fetch --nolog --headers http://www.example.com/  
> {'Accept-Ranges': ['bytes'],  
> 'Age': ['1263 '],  
> 'Connection': ['close '],  
> 'Content-Length': ['596'],  
> 'Content-Type': ['text/html; charset=UTF-8'],  
> 'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],  
> 'Etag': ['"573c1-254-48c9c87349680"'],  
> 'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],  
> 'Server': ['Apache/2.2.3 (CentOS)']}  
  
  
  
下载指定地址的页面，并在本地用浏览器打开
-------------
> scrapy view [options] <url>  
  
Opens the given URL in a browser, as your Scrapy spider would “see” it. Sometimes spiders see pages differently from regular users, so this can be used to check what the spider “sees” and confirm it’s what you expect.  
  
 options:  
--spider=SPIDER: bypass spider autodetection and force use of specific spider  
--no-redirect: do not follow HTTP 3xx redirects (default is to follow them)  
  
例：  
> scrapy view http://www.example.com/some/page.html  
[ ... browser starts ... ]  



