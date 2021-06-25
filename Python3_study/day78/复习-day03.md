

## django回顾

### 1 web应用，http协议，web框架

```python
# ip+端口号唯一确定一个应用
# web框架是什么
# http协议

# wsgi协议，wsgiref，uWSGI分别是什么？
wsgi协议是py中的一个协议：规定了如何拆，封http协议

#模板文件是在什么时候完成渲染的？
在后端渲染完，只要出了django框架，就是完整的html，css和js
```

### 2 django请求生命周期

![1593655165215](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1593655165215.png)

### 3 路由控制

```python
# django是一个同步框架
# 最新版本3.x  
# URL与要为该URL调用的视图函数之间的映射表
# 1.x 和2.x版本路由稍微不同
	1.x：url
    2.x：path，re_path(原来的url)
# 写法
from django.conf.urls import url
urlpatterns = [
     url(正则表达式, views视图函数，参数，别名),
]
#  APPEND_SLASH  的用法
# 
# 有名分组 
re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
# 无名分组
re_path(r'^articles/([0-9]{4})/$', views.year_archive),

# 路由分发
path('app01/', include(urls)),

#反向解析
###视图函数中
from django.shortcuts import reverse
url=reverse('test',args=(10,20))  # test是在url内配置的别名
###在模板中使用
{% url "别名" 参数  参数%}

# 名称空间（了解）

#2.x的path内置了几个转换器
str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
int,匹配正整数，包含0。
slug,匹配字母、数字以及横杠、下划线组成的字符串。
uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
path,匹配任何非空字符串，包含了路径分隔符（/）（不能用？）


# 2.x的path自定义转换器（了解）
```

### 4 视图层

```python
#response对象： 三件套+JsonResponse   本质都是HttpResonse
#request对象：
	request.GET:http://127.0.0.1:8000/index/123?name=lqz&age=18   name=lqz&age=18会被转成字典，放到GET中
    request.POST:urlencoded,formdata两种编码的数据会被放在这个字典中
        
    request.META:HTTP请求的其他东西，放在里面，入客户端ip地址：REMOTE_ADDR
    request.FILES:上传的文件
    request.session:用的session
        
        
# 301 和302的区别

# JsonResponse

# CBV和FBV
#文件上传（form表单中指定编码方式）
def index(request):
    if request.method=='GET':

        return  render(request,'index.html')
    else:
        myfile=request.FILES.get('myfile')  #文件对象
        print(type(myfile))
        from django.core.files.uploadedfile import InMemoryUploadedFile
        name=myfile.name
        print(myfile.field_name)
        with open(name,'wb') as f:
            for line in myfile:
                f.write(line)
        return HttpResponse('文件上传成功')
```

### 5 模板层

```python
模版语法重点：

　　变量：{{ 变量名 }}

　　　　1 深度查询 用句点符

　　　　2 过滤器

　　标签：｛｛%  % ｝｝

	内置过滤器：
    {{obj|filter__name:param}}  变量名字|过滤器名称：变量
    重点：safe
    
    xss攻击
    <a href="https://www.baidu.com">点我<a>  如果原封不动的显示在html中，一定是a标签，html的特殊字符
    
    for标签
    if标签
    with标签
    
    
    # {% csrf_token%}
    {% csrf_token%}
{{ csrf_token }}
<input type="hidden"value="sadfasdfasdf">


# 模板的导入和继承
include
extend：先用{% block title %}，
再用{% extends "base.html" %} 
{% block content %}
自己的内容
{% endblock %}
```

### 6 模型层

```python
# 使用orm的步骤
	1 在setting中配置（连数据库的地址，端口）
    2 在 __init__中使用pymysql
    3 在models.py中写类，写属性
    4 使用：数据库迁移的两条命令
    	python3 manage.py makemigrations  #记录
        python3 manage.py migrate         # 真正的数据库同步
    5 在视图函数中使用orm
    	
 # orm的api
    <1> all():                  查询所有结果

    <2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象

    <3> get(**kwargs):          返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。

    <4> exclude(**kwargs):      它包含了与所给筛选条件不匹配的对象

    <5> order_by(*field):       对查询结果排序('-id')

    <6> reverse():              对查询结果反向排序

    <8> count():                返回数据库中匹配查询(QuerySet)的对象数量。

    <9> first():                返回第一条记录

    <10> last():                返回最后一条记录

    <11> exists():              如果QuerySet包含数据，就返回True，否则返回False

    <12> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                                model的实例化对象，而是一个可迭代的字典序列
    <13> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

    <14> distinct():            从返回结果中剔除重复纪录
        
        
 # 下划线查询
        Book.objects.filter(price__in=[100,200,300])
        Book.objects.filter(price__gt=100)
        Book.objects.filter(price__lt=100)
        Book.objects.filter(price__gte=100)
        Book.objects.filter(price__lte=100)
        Book.objects.filter(price__range=[100,200])
        Book.objects.filter(title__contains="python")
        Book.objects.filter(title__icontains="python")
        Book.objects.filter(title__startswith="py")
        Book.objects.filter(pub_date__year=2012)
 #删除
	对象.delete()   #删一条
    queryset对象.delete()  # 删多条
 #更新
	Book.objects.filter(title__startswith="py").update(price=120）
```





# 作业：

1 链式调用（jq），用python实现链式调用（对象.hello.world.add()）

2 关键字过滤的标签

3 **常用（非常用）字段和参数，Django-model进阶**（https://www.cnblogs.com/liuqingzheng/p/9506212.html）