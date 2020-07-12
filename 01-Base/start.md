  
快速入门地址  
------------
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000   
http://www.runoob.com/python/python-tutorial.html  


快速开始，hello.py
------------
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print('hello, world')
```
执行  
> python hello.py  
  
  
注释  
----------
python中单行注释采用 # 开头。  

python 中多行注释使用三个单引号(''')或三个双引号(""")。 
 
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# 第一个注释
print "Hello, Python!";  # 第二个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```
    
  
    
输入与输出  input()和print()   
------------
输出  
```python
# 最简单的输出，
print('hello, world')
# 输出结果：hello, world
# 或者下面的方式输出，但要注意python3以上版本的，不能用下面的方式，需用print带括号。
print 'hello, world' #python2才能用


# 下面这种print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')
# 输出结果：The quick brown fox jumps over the lazy dog

# 输出一个整型
print(100)

# 计算 100 + 200 然后输出，
print(100 + 200)
# 输出结果：300

print('100 + 200 =', 100 + 200)
# 输出结果： 100 + 200 = 300
```
  
输入  
如果要让用户从电脑输入一些字符怎么办？Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。   
```python
name = input()
print(name)

# 让对方输入前，带上提示文案
name = input('please enter your name: ')
print('hello,', name)
```
  
   
数据类型  
-----------
Python有五个标准的数据类型：  
  
> Numbers（数字）   
> String（字符串）  
> List（列表）  
> Tuple（元组）  
> Dictionary（字典）  


变量声明、赋值
-----------
python声明变量时不用指定变量类型
```python
# 数字
# --------
a1 = 1
a2 = 10
print(a1, a2)


# 字符串
# --------
var1 = 'Hello World!'
var2 = "Python Runoob"
print(var1, var2)

# 可以用方括号来截取字符串
print "var1[0]: ", var1[0]  // 输出 var1[0]:  H
print "var2[1:5]: ", var2[1:5]  // 输出 var2[1:5]:  ytho

# 字符串格式化
# 注意是三个参数：
# 参数1 中带有%xx指定格式，
# 参数2 固定为%，
# 参数3 如果是单个值不用带括号，如果多值需带括事情且用逗号分隔
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。 
hi = '''hi 
there'''
print(hi)


# 列表
# --------
# 与字符串的索引一样，列表索引从0开始
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符 
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
# 以上语句输出结果：
# list1[0]:  physics
# list2[1:5]:  [2, 3, 4, 5]


# 使用append()方法来添加列表项
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print list


# 使用del删除列表的元素
list1 = ['physics', 'chemistry', 1997, 2000]
 
print list1
del list1[2]
print "After deleting value at index 2 : "
print list1


# 元组
# ---------
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

tup3 = tup1 + tup2  # 创建一个新的元组
print tup3


# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组	
tup = ('physics', 'chemistry', 1997, 2000)
print tup
del tup
print "After deleting tup : "
print tup  # 删除后再输出会报异常



# 子典 Dictionary
# ---------
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号{}中。

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];
# 以上实例输出结果：
# dict['Name']:  Zara
# dict['Age']:  7


# 直接通过键值修改
dict['Name'] = 'qianm'
print dict['Name']

# 删除
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典

```
  
  
  
运算符
-----------
算术运算符  
```
以下假设变量： a=10，b=20：
运算符	描述	实例
+	加 - 两个对象相加；	 a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数；	 a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串；	 a * b 输出结果 200
/	除 - x除以y；	 b/a 输出结果 2
%	取模 - 返回除法的余数；	 b % a 输出结果 0
**	幂 - 返回x的y次幂	；   a**b为10的20次方，输出结果 100000000000000000000
//	取整除 - 返回商的整数部分（向下取整）	  9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
```

  
比较（关系）运算符  
```
以下假设变量a为10，变量b为20：

运算符	描述	实例
==	等于 - 比较对象是否相等；	 (a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等；	   (a != b) 返回 true.
<>	不等于 - 比较两个对象是否不相等	；   (a <> b) 返回 true。这个运算符类似 != 。
>	大于 - 返回x是否大于y；	     (a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。   	(a < b) 返回 true。
>=	大于等于	- 返回x是否大于等于y。	     (a >= b) 返回 False。
<=	小于等于 -	返回x是否小于等于y。	 (a <= b) 返回 true。
```

赋值运算符
```
以下假设变量a为10，变量b为20：

运算符	描述	实例
=	简单的赋值运算符	   c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	   c += a 等效于 c = c + a
-=	减法赋值运算符	   c -= a 等效于 c = c - a
*=	乘法赋值运算符	   c *= a 等效于 c = c * a
/=	除法赋值运算符	   c /= a 等效于 c = c / a
%=	取模赋值运算符	   c %= a 等效于 c = c % a
**=	幂赋值运算符		   c **= a 等效于 c = c ** a
//=	取整除赋值运算符	   c //= a 等效于 c = c // a
```

逻辑运算符
```
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

运算符	逻辑表达式	描述	实例
and	  x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	
(a and b) 返回 20。

or	  x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	
(a or b) 返回 10。

not	  not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	
not(a and b) 返回 False
```

位运算符
```
运算符	描述	实例
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	  (a & b) 输出结果 12 ，二进制解释： 0000 1100

|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	 (a | b) 输出结果 61 ，二进制解释： 0011 1101

^	按位异或运算符：当两对应的二进位相异时，结果为1	 (a ^ b) 输出结果 49 ，二进制解释： 0011 0001

~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	 (~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。

<<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	   a << 2 输出结果 240 ，二进制解释： 1111 0000

>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	            a >> 2 输出结果 15 ，二进制解释： 0000 1111
```
  
  
成员运算符  
```
运算符	描述	实例
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。

not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
```
  
  
身份运算符  
```
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
```
  

运算符优先级  
```
以下表格列出了从最高到最低优先级的所有运算符：

运算符		描述
**			指数 (最高优先级)
~ + -		按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -			加法减法
>> <<		右移，左移运算符
&			位 'AND'
^ |			位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符
```
  
  

if语句
--------------
```python
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称
```
   

for语句
--------------
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
```python
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
 
```
  
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
```python
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
```
   

while语句  
--------------
while判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
```
  
while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环
```python
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10
 
i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
```


如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中，类似if
```python
flag = 1
while (flag): print 'Given flag is really true!'
```
  


函数
---------
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。  
```python
# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 缺省参数/默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki" );


# python的函数传参有一种特殊的，关键字传参，如下注意调用时传的参数带了键值
# 关键字传参顺序不重要
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );  
printinfo( name="miki", age=50 ); # 和上面结果一样，顺序不重要



# 不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

```
  
  

面向对象
----------
使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾:  
```python
class Employee:
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)

# 访问类成员
emp1.displayEmployee()
emp2.displayEmployee()

# 可以用类的名称访问类变量
print "Total Employee %d" % Employee.empCount

```
Python内置类属性   
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）  

__doc__ :类的文档字符串  

__name__: 类名  

__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）  

__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）  
  


   
    
日期和时间
---------
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。  
  
```python
import time;  # 引入time模块
 
ticks = time.time()
print "当前时间戳为:", ticks
# 当前时间戳为: 1459994552.51

 

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

# 以上实例输出结果：
# 2016-04-07 10:25:09
# Thu Apr 07 10:25:09 2016
# 1459175064.0



```
  
  
  
python2.x里解决中文乱码的万能钥匙  
--------------
注意，如果是pythons2.x，它的默认编码是ascII，返回的数据可能会乱码。一般情况下我们可以在代码最上方添加：  
```python
import sys
reload(sys)
sys.setdefaultencoding("uft-8")
```
这三行代码是python2.x里解决中文乱码的万能钥匙，python3已解决了此问题，默认编码即unicode。
   
  


















