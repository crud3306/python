参考地址：
----------
https://docs.scrapy.org/en/latest/
https://docs.scrapy.org/en/latest/topics/commands.html （命令行命令）


安装
----------
> pip3 install scrapy
验证是否安装成功，直接在命令行执行scrapy，看是否有信息输出。
> scrapy


原理
----------
scrapy engine:  
负责组件之间数据的流转，当某个动作发生时触发事件  
  
scheduler:  
接收requests，并把他们入队，以便后续的调度  
  
downloader:  
负责抓取网页，并传送给引擎，之后抓取结果将传给spider   
  
spiders:  
用户编补习班的可定制化的部分，负责解析response，产生items和url  
  
item pipeline:  
负责处理item，典型的用途：清洗、验证、持久化  
   
downloader middlewares:  
位于引擎和下载器之间的一个钩子，处理传送到下载器的requests和传送到引擎的response  
  
spider middlewares:  
位于引擎和抓取器之间的一个钩子，片是抓取器的输入和输出  
  
  
scrapy中的数据流执行过程    
注：scrapy中的数据流由引擎控制
1）引擎打开一个网站(open a domain)，找到处理该网站的spider并向该spider请求第一个要爬取的url。   
2）引擎从spider中获取到第一个要爬取的url并在调度器(scheduler)以request调度。  
3）引擎向调度器请求下一个要爬取的url。  
4）调度器返回下一个要爬取的url给引擎，引擎将url通过下载中间件(请求(request)方向)转发给下载器(downloader)  
5）一量页面下载完毕，下载器生成一个该页面的response，并将其通过下载中间件(返回(request)方向)发送给引擎  
6）引擎从下载器中接收到response并通过spider中间件(输入方向)发送给spider外理  
7）spider处理response并返回爬取到的item及(跟进的)新的request给引擎  
8）引擎将(spider返回的)爬取到的item给itempipeline，将(spider返回的)request给调度器  
9）从第二步重复直到调度器中没有更多的request，引擎关闭该网站。  
  
  
  
scrapy爬虫项目一般开发步骤  
---------
scrapy startproject 项目名  
scrapy genspider spider名称 要爬的目标域名(不带http协议)  
编写items.py，明确需要提取的数据  
编写spiders/xxx.py，即编写爬虫文件，处理请求和响应，以及提取数据(yield item)  
编写pipelines.py，编写管道文件，处理spider返回item数据，比如本地持久化存储等...    
编写settings.py，启动管道组件 ITEM_PIPELINES = {...}，以及其它相关设置  
执行爬虫  
  
  


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
  
生成的spider代码为：
----------
```python
import scrapy

class XxxSpider(scrapy.Spider):
	name = "xxxx"
	allowed_domains = ["xxx.com"]
	start_urls = (
		"http://www.xxx.cn/",
	)

	def parse(self, response):
		pass
```
上面的代码是通过命令自动生成的，当然我们也可以手机写上面的代码，只不过使用命令可以免去编写固定代码的麻烦。  
要建立一个Spider，你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性和一个方法。
> name="" 这个爬虫的识别名称，必须是唯一的，同一个scrapy项目中，不同的爬虫必须定义不同的名字。  
> allow_domains=[]是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在url会被忽略。  
> start_urls=() 爬取的URL元组/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
  
  
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
  
执行，并保存结果，四种保存格式：    
> scrapy crawl quotes -o quotes.json    
> scrapy crawl quotes -o quotes.csv  
> scrapy crawl quotes -o quotes.xml  
> scrapy crawl quotes -o quotes.jl  
注意：  
-o 参数，后面通过文件后缀，自动存为各种数据格式的文件。  
  
甚至可指定保存到远程的ftp服务器上  
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
  
  

注意，如果是pythons2.x，它的默认编码是ascII，返回的数据可能会乱码。一般情况下我们可以在代码最上方添加：  
```python
import sys
reload(sys)
sys.setdefaultencoding("uft-8")
```
这三行代码是python2.x里解决中文乱码的万能钥匙，python3已解决了此问题，默认编码即unicode。  
  
  
一些代理ip地址：  
https://www.kuaidaili.com/free/  
http://www.xicidaili.com/  
http://ip.zdaye.com/FreeIPlist.html  

