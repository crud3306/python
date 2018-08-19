#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

# requests 的 response对象
# -----------------
# r.status_code   	http请求的返回状态，200表成功
# r.text 			http响应内容的字符串形式，即请求的url对应的地址返回的内容
# r.encoding 		从http header中猜测的响应内容编码方式
# r.apparent_encoding 从内容中分析出的响应编码方式（备选编码方式）
# r.content 		http响应内容的二进制形式 (比如图片)

# 流程 r.status_code == 200 才取后面的信息 (r.encoding r.apparent_encoding r.content) 

def requestAll(url):
	# requests.request(method, url, **kwargs)
	# -------------
	# method 请求方式，对应get/post/put/patch/delete/header/options 等7种
	# **kwargs 控制访问的参数，共13个：
	# 13个分别为: params, data, json, headers, cookies, auth, files, timeout, proxies, allow_redirects, stream, verify, cert

	# 注意针对 requests.request(method, url, **kwargs)中的method 额外做了封装，可以这样访问:
	# requests.get(url) requests.post(url) requests.put(url) 等7个


	# params
	# kv = { 'k1':'v1', 'k2':'v2' }
	# r = requests.request("get", url, params=kv)
	# print(r.url, r.encoding, r.apparent_encoding)

	# data
	# r = requests.request("post", url, data='123456aaa')
	# print(r.url, r.headers)

	# json
	# kv = { 'k1':'v1', 'k2':'v2' }
	# r = requests.request("get", url, json=kv)
	# print(r.url, r.encoding, r.apparent_encoding)


	# headers 请求头
	# hd = {'user-agent':'Chrome/10'}
	# r = requests.request("post", url, headers=hd)
	# print(r.url, r.headers)

	# proxies 代理
	pxs = {'http': 'http://user:pass@10.10.10.1:1234',
	'https':'https://10.10.10.1:4321'}
	r = requests.request("get", url, proxies=pxs)
	print(r.url, r.headers)


	# fiels 上传文件
	# fs = {'file': open('t.txt', 'rb')}
	# r = requests.request("post", url, files=fs)
	# print(r.url, r.headers)



# 爬取数据时要遵守robots协议，robots exclusion standard 网络爬虫排除标准
# 比如:
# 京东的https://www.jd.com/robots.txt
# 百度的https://www.baidu.com/robots.txt
# 新浪新闻的https://news.sina.com.cn/robots.txt
# qq的https://www.qq.com/robots.txt
# qq新闻的https://news.qq.com/robots.txt

# 通用requests爬虫写法
def getHTMLText(url):
	try:
		headers = {'user-agent':'MOZILLA/5.0'}
		r = requests.get(url, headers=headers, timeout=30)
		# print(r.text)
		r.raise_for_status()
		r.encoding = r.apparent_encoding

		# 可打印出本次请求时带的 request headers。
		print(r.request.headers)

		# 如果仅验证是否请求成功，可以只看返回内容的一部分即可
		return r.text[:1000]
		#return r.text
	except:
		return "产生异常"


# download file
def downloadFile(url):

	_dir  = '/data/www/python/requests/tmp/'
	_file = _dir + url.split('/')[-1]

	try:
		# print('123')
		if not os.path.exists(_dir):
			os.mkdir(_dir)

		print(_file)

		if not os.path.exists(_file):
			headers = {'user-agent':'MOZILLA/5.0'}
			r = requests.get(url, headers=headers, timeout=30)
			# print(r.text)
			r.raise_for_status()
			# r.encoding = r.apparent_encoding

			# 可打印出本次请求时带的 request headers。
			# print(r.request.headers)

			with open(_file, 'wb') as f:
				f.write(r.content)
			f.close()
			print('文件保存成功')

		else:
			print('文件已存在')

		
		
		# 如果仅验证是否请求成功，可以只看返回内容的一部分即可
		# return r.text[:1000]
		#return r.text
	except:
		return "产生异常"


def requestGet(url):
	r = requests.get(url)
	print(r.status_code)

	type(r)

	print(r.headers)
  

if __name__ == '__main__':

	url = "http://www.baidu.com"
	# requestGet(url)
	# requestAll(url)

	# txt = getHTMLText(url)
	# print(txt)

	downloadFile("https://i1.hdslb.com/bfs/archive/7985db97267488e1437e668841d32ae12e5a9f82.jpg@160w_100h.jpg")




















