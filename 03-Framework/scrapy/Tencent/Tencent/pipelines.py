# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import numpy as np #numpy需用pip安装

# 因json.dumps时会报错：Object of type 'bytes' is not JSON serializable
# 所以写了一个MyEncoder，json.dumps(..., cls=MyEncoder)
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


class TencentPipeline(object):
    def __init__(self):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), cls=MyEncoder, ensure_ascii = False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()

