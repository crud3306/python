#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup

# BeautifulSoup的使用
# 先导入 
# from bs4 import BeautifulSoup
# 然后解析远程抓取到的html
# soup = BeautifulSoup("<html><body>12121</body></html>", "html.parser")
# 或者打开一个本地的文件
# soup = BeautifulSoup(open("/data/www/xxx.html", "html.parser")

# BeautifulSoup类的基本元素
# Tag 最基本的信息组成单元，比如html标签
# Name 标签的名字，<p>标签名字p，格式：<tag>.name
# Attributes 标签的属性，字典形式组织，格式：<tag>.attrs
# NavigableString 标签内非属性字符串，<>...</>中间的字符串，格式：<tag>.string
# Comment 标签内字符串的注释部分，一种物殊的Comment类型

# soup.find_all('p',"a")
# soup.find_all(id="xxx")

def requestAll(url):
	pass
	# params
	# kv = { 'k1':'v1', 'k2':'v2' }
	# r = requests.request("get", url, params=kv)
	# print(r.url, r.encoding, r.apparent_encoding)


# 通用requests爬虫写法
def getHTMLText(url):
	try:
		headers = {'user-agent':'MOZILLA/5.0'}
		r = requests.get(url, headers=headers, timeout=30)
		# print(r.text)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		demo = r.text
		soup = BeautifulSoup(demo, 'html.parser')
		# print(soup.prettify())

		print(soup.title, soup.title.name, soup.title.string)
		print(soup.a, soup.a.name, soup.a.parent.name, soup.a.attrs, soup.a.attrs['href'])

		# 更多
		# .parent .parents .contents .children .descendants
		# .next_sibling .previous_sibling .next_siblings .previous_siblings

		# 可打印出本次请求时带的 request headers。
		# print(r.request.headers)

		# 如果仅验证是否请求成功，可以只看返回内容的一部分即可
		# return r.text[:1000]
		# return r.text
	except:
		return "产生异常"



if __name__ == '__main__':

	url = "https://python123.io/ws/demo.html"
	getHTMLText(url)


















