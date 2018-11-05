from multiprocessing import Pool
# from multiprocessing.dummy import Pool
import requests
from requests.exceptions import RequestException
import json
import re

def get_one_page(url):
     try:
          headers = {'user-agent':'MOZILLA/5.0'}
          response = requests.get(url, headers=headers)
          if response.status_code == 200:
               return response.text
          return None
     except RequestException:
          return None

def parse_one_page(html):
     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?interger">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
     #注加上第二个参数re.S，符号.可以匹配换行符。不加不能匹配
     items = re.findall(pattern, html)
     # print(items)
     for item in items:
          yield {
               'index': item[0],
               'image': item[1],
               'title': item[2],
               'actor': item[3].strip()[3:],
               'time': item[4].strip()[5:],
               'score': item[5]+item[6]
          }

def write_to_file(content):
     with open('result.txt', 'a', encoding='utf-8') as f:
          f.write(json.dumps(content, ensure_ascii=False) + '\n')
          f.close()

def main(offset):
     url = 'http://maoyan.com/board/4?offset=' + str(offset)
     html=get_one_page(url)
     print(html)
     #parse_on_page(items)
     # for item in parse_one_page(html):
     #      print(item)
          # write_to_file(item)

if __name__ == '__main__':
     main(0)
     
     #for i in range(10):
     #     main(i*10)
     # 用进程池，多进程处理。问题是顺序会乱
     # pool = Pool()
     # pool = Pool(4) # 可以按电脑内核数指定一个数字，比如4核电脑
     # pool.map(main, [i*10 for i in range(10)])


