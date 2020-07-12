

JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
- json.dumps(): 对数据进行编码。
- json.loads(): 对数据进行解码。



Python 编码为 JSON 类型转换对应表：
```sh
Python									JSON
dict									object
list, tuple								array
str										string
int, float, int- & float-derived Enums	number
True									true
False									false
None									null
```

JSON 解码为 Python 类型转换对应表：
```sh
JSON			Python
object			dict
array			list
string			str
number (int)	int
number (real)	float
true			True
false			False
null			None
```



json.dumps 与 json.loads 处理Json字符串
===========

Python数据结构 转换为 JSON
-----------
实例(Python 3.0+)
```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)


#执行以上代码输出结果为：
Python 原始数据： {'url': 'http://www.runoob.com', 'no': 1, 'name': 'Runoob'}
JSON 对象： {"url": "http://www.runoob.com", "no": 1, "name": "Runoob"}
```

通过输出的结果可以看出，简单类型通过编码后跟其原始的repr()输出结果非常相似。




JSON字符串 转换 Python数据结构
------------
实例(Python 3.0+)
```py
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


#执行以上代码输出结果为：
Python 原始数据： {'name': 'Runoob', 'no': 1, 'url': 'http://www.runoob.com'}
JSON 对象： {"name": "Runoob", "no": 1, "url": "http://www.runoob.com"}
data2['name']:  Runoob
data2['url']:  http://www.runoob.com
```



如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。

json.dump() 和 json.load() 处理文件中的Json数据。
----------
实例(Python 3.0+)
```py
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)
 
# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
```


```python
#coding=utf-8 

import os
import json

#获取目标文件夹的路径
filedir = r'J:\NumberData\mrcnnHik\test'
#获取文件夹中的文件名称列表 
filenames=os.listdir(filedir)

#遍历文件名
for filename in filenames:
  filepath = filedir+'/'+filename
  # print(filepath)
  after = []

  # 打开文件取出数据并修改，然后存入变量
  with open(filepath, 'r') as f:
    data = json.load(f)
    mask=data["MaskPolygonItem"]

    for zidian in mask:
      print(type(zidian))
      mask[zidian]["polygon"] = '354 221,355 310,729 318,733 236'
    after = data

  # 打开文件并覆盖写入修改后内容
  with open(filepath, 'w') as f:
    #结构化写入到文件中
    data = json.dump(after, f, sort_keys=True, indent=4, separators=(',', ': '))
```

原文件内容
```json
{
  "MaskPolygonItem": {
    "0": {
      "BoundingBox": "354.105 221.957 379.764 96.2241",
      "label": "Number",
      "labelNum": 0,
      "polygon": "3,6"
    }
  },
  "channels": 3,
  "height": 1080,
  "width": 1920
}
```

修改后的内容
```json
{
  "MaskPolygonItem": {
    "0": {
      "BoundingBox": "354.105 221.957 379.764 96.2241",
      "label": "Number",
      "labelNum": 0,
      "polygon": "354 221,355 310,729 318,733 236"
    }
  },
  "channels": 3,
  "height": 1080,
  "width": 1920
}
```







