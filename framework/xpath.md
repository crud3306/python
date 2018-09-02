
xpath   
    
参考地址：  
------------
http://www.runoob.com/xpath/xpath-tutorial.html  
http://www.w3school.com.cn/xpath/index.asp  
  
  
先看几个示例：  
假设response是返回的数据  
查找所有含class为even的tr  
> response.xpath("//tr[@class='even']")  
  
查找所有含class为even或odd的tr  
> response.xpath("//tr[@class='even' or @class='odd']")  
  
> response.xpath("//tr[@class='even']/td/a/@href").extract()  
> response.xpath("//tr[@class='even']/td/a/text()").extract()
  
```python
node_list = response.xpath("//tr[@class='even' or @class='odd']")
for node in node_list:
    # 提取每个职位的信息，并且将提取出的unicode字符串转码为utf-8编码
    item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
	# 提取其它更多想要的元素...
```
  
  
xpath介绍  
------------
XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航。  
  
XPath 使用路径表达式在 XML 文档中进行导航  
XPath 包含一个标准函数库  
XPath 是 XSLT 中的主要元素  
XPath 是一个 W3C 标准  
  
节点   
在XPath中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML文档是被作为节点树来对待的。  
  
  
xpath语法  
------------
表达式		描述  
nodename	选取此节点的所有子节点。  
/			从根节点选取。  
//			从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。  
.			选取当前节点。  
..			选取当前节点的父节点。  
@			选取属性。  

例子  
以下面这个xml为例子
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
xml.xpath(“bookstore”) 表示选取 bookstore 元素的所有子节点  
xml.xpath(“/bookstore”) 表示选取根元素 bookstore。  
xml.xpath(“bookstore/book”) 选取属于 bookstore 的子元素的所有 book 元素。  
xml.xpath(“//book”) 选取所有 book 子元素，而不管它们在文档中的位置。  
xml.xpath(“bookstore//book”) 选择属于 bookstore 元素的后代的所有 book   元素，而不管它们位于 bookstore 之下的什么位置。  
xml.xpath(“//@lang”) 选取名为 lang 的所有属性。  
  

谓语  
路径表达式					结果  
/bookstore/book[1]			选取属于 bookstore 子元素的第一个 book 元素。
/bookstore/book[last()]		选取属于 bookstore 子元素的最后一个 book 元素。
/bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
/bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。  
//title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。  
//title[@lang=’eng’]	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。  
/bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。  
/bookstore/book[price>35.00]/title   选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。  
  
选取未知节点   
通配符		描述   
*			匹配任何元素节点。  
@*			匹配任何属性节点。  
node()		匹配任何类型的节点。  
  
例子：  
路径表达式		结果    
/bookstore/*	选取 bookstore 元素的所有子元素。  
//*				选取文档中的所有元素。  
//title[@*]		选取所有带有属性的 title 元素。  

选取若干路径  
通过在路径表达式中使用“|”运算符，您可以选取若干个路径。  
  
//book/title | //book/price 选取 book 元素的所有 title 和 price 元素。  
//title | //price 选取文档中的所有 title 和 price 元素。  
/bookstore/book/title | //price 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。 


轴
------------
轴可定义相对于当前节点的节点集。
  
轴名称		结果  
ancestor    选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute	选取当前节点的所有属性。
child		选取当前节点的所有子元素。
descendant  选取当前节点的所有后代元素（子、孙等）。
descendant-or-self  选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following   选取文档中当前节点的结束标签之后的所有节点。
namespace   选取当前节点的所有命名空间节点。
parent      选取当前节点的父节点。
preceding   选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling   选取当前节点之前的所有同级节点。
self 		选取当前节点。
  
  
步的语法：   
轴名称::节点测试[谓语]  
  
例子：  
  
例子				结果  
child::book 	选取所有属于当前节点的子元素的 book 节点。
attribute::lang 选取当前节点的 lang 属性。
child::*		选取当前节点的所有子元素。
attribute::*	选取当前节点的所有属性。
child::text()	选取当前节点的所有文本子节点。
child::node()	选取当前节点的所有子节点。
descendant::book	选取当前节点的所有 book 后代。
ancestor::book      选择当前节点的所有 book 先辈。
ancestor-or-self::book  选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
child::*/child::price   选取当前节点的所有 price 孙节点。
  
  
一些函数  
------------
1. starts-with函数  
获取以xxx开头的元素   
例子：xpath(‘//div[stars-with(@class,”test”)]’)  
  
2 contains函数  
获取包含xxx的元素   
例子：xpath(‘//div[contains(@id,”test”)]’)  
  
3 and  
与的关系   
例子：xpath(‘//div[contains(@id,”test”) and contains(@id,”title”)]’)  
  
4 text()函数  
例子1：xpath(‘//div[contains(text(),”test”)]’)   
例子2：xpath(‘//div[@id="test"]/text()’)  
   
一个lxml的xpath示例  
------------
```python
#coding=utf-8

from lxml import etree

html = '''
<html>
　　<head>
　　　　<meta name="content-type" content="text/html; charset=utf-8" />
　　　　<title>友情链接查询 - 站长工具</title>
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
　　　　<meta name="Keywords" content="友情链接查询" />
　　　　<meta name="Description" content="友情链接查询" />

　　</head>
　　<body>
　　　　<h1 class="heading">Top News</h1>
　　　　<p style="font-size: 200%">World News only on this page</p>
　　　　Ah, and here's some more text, by the way.
　　　　<p>... and this is a parsed fragment ...</p>

　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a> 
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a> 
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a> 
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a> 
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>

　　</body>
</html>
'''
page = etree.HTML(html.lower().decode('utf-8'))
hrefs = page.xpath(u"//a")
for href in hrefs:
    print href.attrib
```  
打印出的结果为：  
{‘href’: ‘http://www.cydf.org.cn/‘, ‘target’: ‘_blank’, ‘rel’: ‘nofollow’}   
{‘href’: ‘http://www.4399.com/flash/32979.htm‘, ‘target’: ‘_blank’}   
{‘href’: ‘http://www.4399.com/flash/35538.htm‘, ‘target’: ‘_blank’}   
{‘href’: ‘http://game.3533.com/game/‘, ‘target’: ‘_blank’}   
{‘href’: ‘http://game.3533.com/tupian/‘, ‘target’: ‘_blank’}   
{‘href’: ‘http://www.4399.com/‘, ‘target’: ‘_blank’}   
{‘href’: ‘http://www.91wan.com/‘, ‘target’: ‘_blank’}  
  
如果要获取标签a之间的内容，就可以用print href.text输出  
  
总结  
--------
上面的内容大多都是抄自网上的一些资料。这里只是做了一个大概的总结，后面如果有漏的还会补充。   





