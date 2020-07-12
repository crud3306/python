


jsonpath安装
--------
> pip install jsonpath


示例
--------
```py
#代码
import jsonpath

dic =   {
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2057,
                        "name": "xiaohei",
                        "sex": "nan",
                        "age": 29,
                        "addr": "beijing",
                        "grade": "tianxie",
                        "phone": "18712321234",
                        "gold": 100
                }
        ]
}

s = jsonpath.jsonpath(dic,'$..name')   #不管有多少层，写两个.都能取到
print(s) #['xiaohei'] 返回的是一个列表
s = jsonpath.jsonpath(dic,'$..hehe')   #当不存在hehe这个key时，返回false
print(s)  #False
```

