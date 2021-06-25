# 本周内容

### django-rest-framework

### restful规范，

### drf入门，

### 视图，

### 序列化（最重要）

### 响应，

### 权限，

### 认证

### 频率，

### 过滤，

### 分页

## 今日内容

## 1 web开发模式

```python
#前后端混合开发（前后端不分离）：返回的是html的内容，需要写模板
#前后端分离：只专注于写后端接口，返回json，xml格式数据

# xml格式
<xml>
<name>lqz</name>
</xml>
# json
{"name":"lqz"}

# java---》jsp
https://www.pearvideo.com/category_loading.jsp
#php写的
http://www.aa7a.cn/user.php
# python写的
http://www.aa7a.cn/user.html




#什么是动态页面（查数据库的），什么是静态页面（静止的html）
#页面静态化
```

### 2 api接口

```python
#通过网络，规定了前后台信息交互规则的url链接，也就是前后台信息交互的媒介

#百度地图的api接口 
https://api.map.baidu.com/place/v2/search?ak=6E823f587c95f0148c19993539b99295&region=%E4%B8%8A%E6%B5%B7&query=%E8%82%AF%E5%BE%B7%E5%9F%BA&output=xml
```

## 3 postman的使用

```python
# postman是目前最好用的，模拟发送http请求的工具
# 双击安装，安装完成自动打开

# 解析json的网站
http://www.json.cn/
    
#请求头中User-Agent：客户端的类型
# 请求头中加其他参数：
# 批量接口导出和测试（实操一下）


```

![1594001178121](.\assets\1594001228907.png)



## 4 Restful规范（重点）

```python
REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征性状态转移）。 它首次出现在2000年Roy Fielding的博士论文中。

RESTful是一种定义Web API接口的设计风格，尤其适用于前后端分离的应用模式中。

这种风格的理念认为后端开发任务就是提供数据的，对外提供的是数据资源的访问接口，所以在定义接口时，客户端访问的URL路径就表示这种要操作的数据资源。

事实上，我们可以使用任何一个框架都可以实现符合restful规范的API接口。

# 抓包工具：fiddler，charles

# 10条规范
1  数据的安全保障：url链接一般都采用https协议进行传输 注：采用https协议，可以提高数据交互过程中的安全性
2 接口特征表现，一看就知道是个api接口
    - 用api关键字标识接口url：
      - [https://api.baidu.com](https://api.baidu.com/)
      - https://www.baidu.com/api
      注：看到api字眼，就代表该请求url链接是完成前后台数据交互的
      -路飞的接口：https://api.luffycity.com/api/v1/course/free/
3 多数据版本共存
    - 在url链接中标识数据版本
    - https://api.baidu.com/v1
    - https://api.baidu.com/v2
    注：url链接中的v1、v2就是不同数据版本的体现（只有在一种数据资源有多版本情况下）
4 数据即是资源，均使用名词（可复数）
    - 接口一般都是完成前后台数据的交互，交互的数据我们称之为资源
      - https://api.baidu.com/users
      - https://api.baidu.com/books
      - https://api.baidu.com/book

      注：一般提倡用资源的复数形式，在url链接中奖励不要出现操作资源的动词，错误示范：https://api.baidu.com/delete-user
    - 特殊的接口可以出现动词，因为这些接口一般没有一个明确的资源，或是动词就是接口的核心含义

      - https://api.baidu.com/place/search
      - https://api.baidu.com/login
5 资源操作由请求方式决定（method）
    - 操作资源一般都会涉及到增删改查，我们提供请求方式来标识增删改查动作
      - https://api.baidu.com/books - get请求：获取所有书
      - https://api.baidu.com/books/1 - get请求：获取主键为1的书
      - https://api.baidu.com/books - post请求：新增一本书书
      - https://api.baidu.com/books/1 - put请求：整体修改主键为1的书
      - https://api.baidu.com/books/1 - patch请求：局部修改主键为1的书
      - https://api.baidu.com/books/1 - delete请求：删除主键为1的书
6 过滤，通过在url上传参的形式传递搜索条件
    - https://api.example.com/v1/zoos?limit=10：指定返回记录的数量
    - https://api.example.com/v1/zoos?offset=10：指定返回记录的开始位置
    - https://api.example.com/v1/zoos?page=2&per_page=100：指定第几页，以及每页的记录数
    - https://api.example.com/v1/zoos?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序
    - https://api.example.com/v1/zoos?animal_type_id=1：指定筛选条件
        
7 响应状态码
   7.1 正常响应
    - 响应状态码2xx
      - 200：常规请求
      - 201：创建成功
   7.2 重定向响应
    - 响应状态码3xx
      - 301：永久重定向
      - 302：暂时重定向
   7.3 客户端异常
    - 响应状态码4xx
      - 403：请求无权限
      - 404：请求路径不存在
      - 405：请求方法不存在
	7.4 服务器异常
    - 响应状态码5xx
      - 500：服务器异常
 8 错误处理，应返回错误信息，error当做key
    {
        error: "无权限操作"
    }
    
 9 返回结果，针对不同操作，服务器向用户返回的结果应该符合以下规范
    GET /collection：返回资源对象的列表（数组）
    GET /collection/resource：返回单个资源对象
    POST /collection：返回新生成的资源对象
    PUT /collection/resource：返回完整的资源对象
    PATCH /collection/resource：返回完整的资源对象
    DELETE /collection/resource：返回一个空文档
    
 10 需要url请求的资源需要访问资源的请求链接
     # Hypermedia API，RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么
        {
            "status": 0,
            "msg": "ok",
            "results":[
                {
                    "name":"肯德基(罗餐厅)",
                    "img": "https://image.baidu.com/kfc/001.png"
                }
                ...
                ]
        }
```



## 5 drf的安装和简单使用

```python
# 安装：pip install djangorestframework==3.10.3
# 使用
	1 在setting.py 的app中注册
        INSTALLED_APPS = [
        'rest_framework'
        ]
    2 在models.py中写表模型
    	class Book(models.Model):
            nid=models.AutoField(primary_key=True)
            name=models.CharField(max_length=32)
            price=models.DecimalField(max_digits=5,decimal_places=2)
            author=models.CharField(max_length=32)
    3 新建一个序列化类（听不懂）
    	from rest_framework.serializers import ModelSerializer
        from app01.models import  Book
        class BookModelSerializer(ModelSerializer):
            class Meta:
                model = Book
                fields = "__all__"
    4 在视图中写视图类
        from rest_framework.viewsets import ModelViewSet
        from .models import Book
        from .ser import BookModelSerializer
        class BooksViewSet(ModelViewSet):
            queryset = Book.objects.all()
            serializer_class = BookModelSerializer
    5 写路由关系
    	from app01 import views
        from rest_framework.routers import DefaultRouter
        router = DefaultRouter()  # 可以处理视图的路由器
        router.register('book', views.BooksViewSet)  # 向路由器中注册视图集
          # 将路由器中的所以路由信息追到到django的路由列表中
        urlpatterns = [
            path('admin/', admin.site.urls),
        ]
        #这是什么意思？两个列表相加
        # router.urls  列表
        urlpatterns += router.urls
        
    6 启动，在postman中测试即可
```



## 3 cbv源码

```python
# ModelViewSet继承View（django原生View）
# APIView继承了View

# 先读View的源码
from django.views import View

# urls.py
path('books1/', views.Books.as_view()),  #在这个地方应该写个函数内存地址,views.Books.as_view()执行完，是个函数内存地址,as_view是一个类方法，类直接来调用，会把类自动传入
放了一个view的内存地址（View--》as_view--》内层函数）

# 请求来了，如果路径匹配，会执行，  函数内存地址(request)
def view(request, *args, **kwargs):
    #request是当次请求的request
    self = cls(**initkwargs)  #实例化得到一个对象，Book对象
    if hasattr(self, 'get') and not hasattr(self, 'head'):
        self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return self.dispatch(request, *args, **kwargs)

 
def dispatch(self, request, *args, **kwargs):
		#request是当次请求的request   self是book对象
        if request.method.lower() in self.http_method_names:
            #handler现在是：
            handler=getattr(self,'get'),你写的Book类的get方法的内存地址
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)  #执行get(request)
```







## 4 APIView源码分析

```python
#from rest_framework.views import APIView
# urls.py
path('booksapiview/', views.BooksAPIView.as_view()),  #在这个地方应该写个函数内存地址

#APIView的as_view方法（类的绑定方法）
   def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)  # 调用父类（View）的as_view(**initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs
        # 以后所有的请求，都没有csrf认证了，只要继承了APIView，就没有csrf的认证
        return csrf_exempt(view)
 

#请求来了---》路由匹配上---》view（request）---》调用了self.dispatch(),会执行apiview的dispatch
    
# APIView的dispatch方法
    def dispatch(self, request, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        # 重新包装成一个request对象，以后再用的request对象，就是新的request对象了
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            # 三大认证模块
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            # 响应模块
            response = handler(request, *args, **kwargs)

        except Exception as exc:
            # 异常模块
            response = self.handle_exception(exc)

        # 渲染模块
        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response
   
# APIView的initial方法
 	def initial(self, request, *args, **kwargs):
        # 认证组件：校验用户 - 游客、合法用户、非法用户
        # 游客：代表校验通过，直接进入下一步校验（权限校验）
        # 合法用户：代表校验通过，将用户存储在request.user中，再进入下一步校验（权限校验）
        # 非法用户：代表校验失败，抛出异常，返回403权限异常结果
        self.perform_authentication(request)
        # 权限组件：校验用户权限 - 必须登录、所有用户、登录读写游客只读、自定义用户角色
        # 认证通过：可以进入下一步校验（频率认证）
        # 认证失败：抛出异常，返回403权限异常结果
        self.check_permissions(request)
        # 频率组件：限制视图接口被访问的频率次数 - 限制的条件(IP、id、唯一键)、频率周期时间(s、m、h)、频率的次数（3/s）
        # 没有达到限次：正常访问接口
        # 达到限次：限制时间内不能访问，限制时间达到后，可以重新访问
        self.check_throttles(request)
```



```python

from rest_framework.request import Request
# 只要继承了APIView，视图类中的request对象，都是新的，也就是上面那个request的对象了
# 老的request在新的request._request
# 以后使用reqeust对象，就像使用之前的request是一模一样（因为重写了__getattr__方法）
  def __getattr__(self, attr):
        try:
            return getattr(self._request, attr) #通过反射，取原生的request对象，取出属性或方法
        except AttributeError:
            return self.__getattribute__(attr)

 # request.data 感觉是个数据属性，其实是个方法，@property，修饰了
	它是一个字典，post请求不管使用什么编码，传过来的数据，都在request.data
 #get请求传过来数据，从哪取？
	request.GET
    @property
    def query_params(self):
        """
        More semantically correct name for request.GET.
        """
        return self._request.GET
    
    #视图类中
     print(request.query_params)  #get请求，地址中的参数
     # 原来在
     print(request.GET)

```





# 补充



## 1 查看源码

![1594007392443](.\assets\1594007392443.png)

## 2 一切皆对象

```python
def foo(a,b):
    return a+b

foo.name='lqz'  #由于一切皆对象，函数也是个对象，对象放值

print(foo(2,3))

print(foo.name)
```

## 3 局部禁用csrf

```python
# 在视图函数上加装饰器@csrf_exempt
# csrf_exempt(view)这么写和在视图函数上加装饰器是一毛一样的

#urls.py中看到这种写法
path('tset/', csrf_exempt(views.test)),
```



## 作业

## 1 用postman，用django写几个接口，测试，导出文件

## 2 新建一个图书表，5个符合restful规范的接口，用CBV的APIView实现

## 3 rest_framework的Resquest类和APIView类，流程，你走一遍，整理成自己的话







