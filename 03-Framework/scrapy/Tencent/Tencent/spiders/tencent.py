# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    # 爬虫名(必须)
    name = 'tencent'
    # 爬虫爬取数据域范围(可选)
    allowed_domains = ['tencent.com']

    baseUrl = "https://hr.tencent.com/"
    startUrl = baseUrl + "position.php?&start="
    offset = 0
    
    # 爬虫启动时，读取的url地址列表(必须)
    start_urls = [startUrl + str(offset)]

    def parse(self, response):
        # print(response.url, response)
        # 提取每个url请求返回的response数据
        node_list = response.xpath("//tr[@class='even' or @class='odd']")
        for node in node_list:
            # 构建item对旬，此对象在items.py中
            item = TencentItem()

            # 提取每个职位的信息，并且将提取出的unicode字符串转码为utf-8编码
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")

            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item['positionType'] = ""

            item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")

            yield item

        # 第一种写法：拼接url
        # 适用场景：页面没有可以点击的请求链接，必须通过拼接url才能获取响应
        # if self.offset < 2190:
        #     self.offset += 10
        #     url = self.startUrl + str(self.offset)
        #     yield scrapy.Request(url, callback = self.parse)

        # 第二种写法：直接从response获取需要爬取的链接，并发起请求处理，直到链接全部提取完毕
        # 适用场景：页面有可以点击的请求链接，比如持续爬取页面中的下一页链接，直到没有下一页为止
        if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0 and len(response.xpath("//a[@id='next']/@href")) != 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            # 可以不用加callback = self.parse，因scrapy.Request默认的回调就是self.parse
            yield scrapy.Request(self.baseUrl + url, callback = self.parse)    

	# def parse_next(self, response):
	# 	pass	





























