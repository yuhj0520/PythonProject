# 今日内容

## 1 个人介绍

刘清政，刘老师，老刘 ，Justin

##  2 关于编辑器

python开发：pycharm（收费），vscode（免费），sublintext，

go开发：goland（收费），vscode，国产的

java：idea（收费），eclipse（免费），MyEclipse（收费）

android：androidstudio（免费），eclipse+adt

前端：webstorm（收费）

php：phpstorm（收费）

数据库开发：data

jetbrains公司出的全家桶，一个注册码，可以都用

androidstudio：买了jetbrains公司授权，在它基础上，做了它

## 3  基础串讲

### 3.1 解释型和编译型

```python
# 你出去之后开发环境：windows开发（主流），sanic，fastapi框架，windows安装不上（不支持），装了乌班图，在上面开发，配mac本
# 远程连接linux开发，远程连linux内的docker开发


c：c代码写完，编译（不同平台），跨平台运行，linux上源码安装软件，自行编译，运行
java:一处编码，处处运行，java是编译型还是解释型？编译型，编译过程---把java源代码编译成字节码文件 .class
    ---不能直接运行在操作系统之上----》jvm（java虚拟机），jvm运行至少要300m内存
    jdk
    jre
    jvm
    javase javame javaee
go:编译型，跨平台编译（windows平台可以编译出mac平台的可执行文件），所有go代码打成一个可执行文件
    
python: 强类型动态语言
js：只能在浏览器中运行，nodejs
php：web开发


# 你们将来从从事的方向
1 python后端开发：做网站，前端可以是app，小程序的python后端
2 自动化运维：收集服务器软硬件信息（cmdb），jumpserver（堡垒机），sql审批，监控，日志收集，处理
devops：ci/di

3 自动化测试：selenium，appnium，pytest
4 数据分析：
5 爬虫：
6 量化交易
7 人工智能，图像处理
8 安全方向：端口扫描，弱口令扫描，sql注入，csrf攻击，xss攻击（利用python成为顶级黑客）
9 网络方向
10 物联网方向

# 申请一个github账号
# 维护一个博客（博客园，自己写的，hexo）

```

## 3.2 数据类型



#### 3.2.1 一切皆对象

```python
python中一切皆对象

# type和object的关系
1 type 是object的类
2 type继承了object
3 type是type自己的类
4 object也是由type实例化得到


a=int(2)
#int是一个类，具体实现是由c语言实现的，如果写了pass，看不到源码,有一部分可以看到
# print(type(1))  # int :数字1 的类是int
#
# print(type(int))
# print(type(dict))

# int。dict..都是type类的对象
# int。dict继承了object
# type和object是什么关系？

# print(type(object))
# print(type(type))
# object

def a():
    pass

print(type(a))



print(type(int))  #type
print(type(object))  #type
print(type(type))  #type

# 所有类，除了object都继承自object，包括type


```

#### 3.2.1 深浅copy

```python
 #一切皆对象的好处
不同类型之间的变量直接可以相关赋值
a=100
a='xxx'
其实本质，变量都是指向了一个内存地址
出现了深浅copy问题
# 深浅copy问题

# l=[1,2,3,[4,5,6]]
# l2=l  #赋值
#
# print(l2 is l)
# from copy import copy
# from copy import deepcopy
# # l3=copy(l)
# # print(l)
# # print(l3)
# # print(l is l3)
# # l3[3][1]=999
# # print(l)
# # print(l3)
#
# l4=deepcopy(l)
# l4[3][1]=999
# print(l)
# print(l4)

```

### 3.2.3 可变类型与不可变类型

```python
#字典，列表，集合   可变类型
#数字，字符串，元组  不可变类型
# 字典的key必须用不可变类型，可以hash    
# 看一下这篇博客
https://www.cnblogs.com/xiaoyuanqujing/articles/12008689.html
# python中的参数传递是值传递还是引用传递？
python中参数传递都是copy一份传递过去，由于一切皆对象，传过去，都是地址，python中区分可变和不可变类型，可变类型在函数中修改会影响原来的，不可变类型，不会影响原来的
```

### 3.3 字符编码

```python
# 计算机的计量单位：
bit比特位：0或者1的一个小格
8个bit位是一个byte，一个字节
1024个字节---》1kb
1024kb---》1mb
1024mb---》1gb

1个字节---》2的8次方中变化，就可以表示出所有的字符（数字，字母，标点符号）

计算机到了中国---》中国汉字--》gbk编码
但是到了不同国家，不同国家有不同国家编码方式，就会出现乱码问题

Unicode编码统一了，字符和数字的对应关系

utf-8：目前主流的编码方式
utf-16

需要说清楚：assic码，gbk，unicode，utf-8
```

## 3.4 闭包函数

```python
1 定义在函数内部
2 对外部作用域有引用

函数是一等公民：函数可以赋值给一个变量
# 装饰器是闭包函数的典型应用
# python中有装饰器语法糖  @

def wrapper(func):
    def inner(*args,**kwargs):
        # 代码
        res=func(*args,**kwargs)
        # 代码
        return res
    return inner

# def a():
#     print("xxx")
   
# 没有语法糖 
# a=wrapper(a)
# a()

# 有语法糖
# @wrapper()
def a():
    print("xxx")
    
# 面向切面编程 AOP
# OOP 面向对象编程

```













## 作业

```python
前后端传数据三种编码格式，传json格式，原生django不能从POST中取出字典
用中间件或者装饰器前端不管传json还是其他格式，requests对象中有个data属性
```

