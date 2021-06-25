# 今日内容

## 1 后续课程安排

```python
1 drf框架
2 git
3 redis使用
4 路飞项目（celery异步）
5 爬虫（mongodb）
6 linux
7 cmdb项目（资产收集）
8 代码发布系统
9 flask框架（给你一到两个项目）
10 数据结构和算法
11 docker，dockercompose（用docker部署项目，nginx负载均衡，横向扩展），k8s(看情况)
12 就业辅导（redis高级，Elasticsearch，如何提高项目并发量，分布式锁，分布式id，远程连接docker开发，git冲突如何解决）
```

## 2 作业讲解

```python
#django.middleware.common.CommonMiddleware 中间件源码

# 核心代码（中间件）
from django.utils.deprecation import MiddlewareMixin

import json
class JsonMiddel(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.data=json.loads(request.body)
        except Exception as e:
            request.data=request.POST
            
# 关注的问题：
1 form表达和ajax提交的重复，form表单中input的submit类型和button按钮都会触发两次（有ajax的情况），input的button类型
2 from django.http.request import QueryDict 
	本质就是一个字典，比字典强大。不能修改值，一改就报错
3 CommonMiddleware中间件控制了是否重定向到带/的地址
```



## 3 python中的魔法方法

``` python
# __init__：类实例化会触发
# __str__:打印对象会触发
# __call__:对象()触发，类也是对象  类(),类的实例化过程调用元类的__call__
# __new__:在类实例化会触发，它比__init__早（造出裸体的人，__init__穿衣服）
# __del__:del 对象，对象回收的时候触发
# __setattr__,__getattr__:(.拦截方法)，当对象.属性--》赋值会调用setattr，如果是取值会调用getattr
# __getitem__,__setitem__:([]拦截)
# __enter__和__exit__ 上下文管理器

```







#### setattr，getattr，setitem，getitem演示

```python


# class Person:
#     def __init__(self,name):
#         self.name=name
#     def __setitem__(self, key, value):
#         setattr(self,key,value)  #反射
#     def __getitem__(self, item):
#         return getattr(self,item) # 反射取值
#
# p=Person('lqz')
# # p.name='ppp'
# p['name']=10 # 如何变行 重写__setitem__魔法方法
# # print(p.name)
#
# print(p['name'])


# dic={'name':'lqz','age':19}

class Mydic(dict):
    def __setattr__(self, key, value):
        print("对象加点赋值，会触发我")
        self[key]=value
    def __getattr__(self, item):
        print("对象加点取值，会触发我")
        return self[item] # 不要加引号

mydic=Mydic(name='lqz',age=18)
# print(mydic['name'])
print(mydic.name)
# mydic.name=99
# print(mydic.name)
```





#### with 上下文管理器

```python
class Person:
    def __enter__(self):
        print("我在with管理的时候，会触发")
        print('进入with语句块时执行此方法，此方法如果有返回值会赋值给as声明的变量')
        return 'oo'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出with代码块时执行此方法')
        print('1', exc_type)
        print('2', exc_val)
        print('3', exc_tb)


with Person() as p:   # 这句话执行，会触发类的__enter__
    print(p)
```

#### __eq__

```python
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # def __eq__(self,obj):
    #     # 打印出比较的第二个对象的x值
    #     print(obj.x)
    #     if self.x +self.y == obj.x+obj.y:
    #         return True
    #     else:
    #         return False

a=A(1,2)
b=A(99,3)
print(a=='ddd')   # 当执行==s时，会触发__eq__的执行，并且把b传进去，就是object
# ==后只要是对象，就可以传进去，就是object

```



## 4   cookie，session，token

```python
# HTTP协议：无状态，无连接，基于请求响应，基于tcp/ip,应用层协议

# mysql：c/s架构：底层基于socket，自己封装的协议，mysql的客户端：navcate（c++图形化界面，实现了请求和响应协议）,pymysql(用python语言实现了请求和响应协议)
# redis：c/s架构：底层基于socket，自己封装的协议
# docker：c/s架构，基于http协议，使用restfull规范
# elasticsearch：c/s架构，基于http协议，使用restfull规范

# cookie：是存在于浏览器的键值对，向服务端发送请求，携带它过去（不安全）
# session：存在于服务端的键值对（放在哪？内存中，文件，mysql，redis）
#  缺陷：如果用户量很大，存储需要耗费服务器资源
# token：就是个字符串（既安全，又存个人信息），加密字符串，会有个人信息

# token现在应用非常广泛，契合了前后端分离
# JWT：json web token
```

### 5 django中的session底层原理

```python
# 在中间件中，请求走的时候，process_response，取出request.session的modify属性，判断是否是true，如果是true，表示在视图函数中修改过session，数据库同步修改，如果是false，就不修改，返回给前端sessionid：随机字符串
# 请求来了，通过sessionid，取出随机字符串--》去数据库中查--》把表的数据转成字典，赋值给request.session,后面视图函数中就可以操作它了
```



### 6 异常处理

```python
try:
except   ：
finally：
else：  什么时候执行


try:
    print("xxx")
    # print(1/0)
except Exception as e:
    print(e)
else:  # 基本上不会用到
    print("正常执行，没有出异常，会走")
finally:
    print("我是finally")   # 用于会走，无论是否有异常
```

## 7 pymysql的使用

```python
import pymysql


#连接数据库
conn=pymysql.connect(host='101.133.225.166', user='root', password="123456",database='test', port=3306) #
# 获取游标
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) # 查出来数据是字典格式
# 操作 定义一个sql
# sql='select id,name from book'
# cursor.execute(sql)
# ret=cursor.fetchall()
# print(ret)
# 插入
# sql='insert into book(id,name) values (%s,%s)'
# cursor.execute(sql,[3,'lqz'])
# conn.commit()

# 删除
# sql='delete from book where name=%s'
# cursor.execute(sql,['lqz'])
# conn.commit()

# 更新
# sql='update book set name=%s where id=%s'
# cursor.execute(sql,['xxx',1])
# conn.commit()
```





# 作业

1 写一个类，有个name属性，如果name赋值为非字符串，就不让放

2 通过上下文管理器写一个mysql的连接，通过with管理

3 使用django实现token功能