#  昨日回顾

```python
# 1 路由
# 2 3种写法  
	-django传统的路由（cvb路由）path('test/', views.TestView.as_view()),
    -只要继承ViewSetMixin：path('books/', views.BookViewSet.as_view({'get':'list','post':'create'})),
    -自动生成路由
    	-SimpleRouter
        -DefaultRouter
        -使用：
        	# 第一步：导入routers模块
            from rest_framework import routers
            # 第二步：有两个类,实例化得到对象
            # routers.DefaultRouter 生成的路由更多
            # routers.SimpleRouter
            router=routers.SimpleRouter()
            # 第三步：注册
            # router.register('前缀','继承自ModelViewSet视图类','别名')
            router.register('books',views.BookViewSet) # 不要加斜杠了
            urlpatterns+=router.urls
#3 action的使用：装饰器给继承了ModeViewSet的视图类中自定义的方法，自动生成路由
#4 method=['get','post'],detail=True(带pk的)/False（不带pk）

# 5 认证
	-使用
    	-定义一个类，继承BaseAuthentication，重写def authenticate(self, request)，校验成功返回两个值，一个是user对象，第二个是token
        -需要注意，如果配置多个认证类，要把返回两个值的放到最后
        -全局使用：setting配置
            REST_FRAMEWORK={
        	"DEFAULT_AUTHENTICATION_CLASSES":["app01.app_auth.MyAuthentication",],
    			}
        -局部使用：
        authentication_classes=[MyAuthentication]
        -局部禁用：authentication_classes = []
```



##  今日内容

## 1 权限

### 1.1 权限源码分析

```python

# APIView---->dispatch---->initial--->self.check_permissions(request)(APIView的对象方法)
    def check_permissions(self, request):
        # 遍历权限对象列表得到一个个权限对象(权限器)，进行权限认证
        for permission in self.get_permissions():
            # 权限类一定有一个has_permission权限方法，用来做权限认证的
            # 参数：权限对象self、请求对象request、视图类对象
            # 返回值：有权限返回True，无权限返回False
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                )
```

## 1.2 权限的使用

```python
# 写一个类，继承BasePermission，重写has_permission，如果权限通过，就返回True，不通过就返回False
from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def  has_permission(self, request, view):
        # 不是超级用户，不能访问
        # 由于认证已经过了，request内就有user对象了，当前登录用户
        user=request.user  # 当前登录用户
        # 如果该字段用了choice，通过get_字段名_display()就能取出choice后面的中文
        print(user.get_user_type_display())
        if user.user_type==1:
            return True
        else:
            return False
        
# 局部使用
class TestView(APIView):
    permission_classes = [app_auth.UserPermission]
# 全局使用
REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":["app01.app_auth.MyAuthentication",],
    'DEFAULT_PERMISSION_CLASSES': [
        'app01.app_auth.UserPermission',
    ],
}
# 局部禁用
class TestView(APIView):
    permission_classes = []
```

### 1.3 内置权限（了解）

```python
# 演示一下内置权限的使用：IsAdminUser，控制是否对网站后台有权限的人
# 1 创建超级管理员
# 2 写一个测试视图类
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
class TestView3(APIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAdminUser]
    def get(self,request,*args,**kwargs):
        return Response('这是22222222测试数据，超级管理员可以看')
# 3 超级用户登录到admin，再访问test3就有权限
# 4 正常的话，普通管理员，没有权限看（判断的是is_staff字段）
```



## 2 频率

### 2.1 内置的频率限制(限制未登录用户)

```python
# 全局使用  限制未登录用户1分钟访问5次
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/m',
    }
}
##############views.py
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
class TestView4(APIView):
    authentication_classes=[]
    permission_classes = []
    def get(self,request,*args,**kwargs):
        return Response('我是未登录用户')

# 局部使用
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.throttling import AnonRateThrottle
class TestView5(APIView):
    authentication_classes=[]
    permission_classes = []
    throttle_classes = [AnonRateThrottle]
    def get(self,request,*args,**kwargs):
        return Response('我是未登录用户，TestView5')
```

### 2.2 内置频率限制之，限制登录用户的访问频次

```python
# 需求：未登录用户1分钟访问5次，登录用户一分钟访问10次
全局：在setting中
  'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '10/m',
        'anon': '5/m',
    }
        
 局部配置：
	在视图类中配一个就行
```



## 3 过滤

```python
#1 安装：pip3 install django-filter
#2 注册，在app中注册
#3 全局配，或者局部配
 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
#4 视图类
class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('name',)  #配置可以按照哪个字段来过滤
```



## 4 排序

```python
# 局部使用和全局使用
# 局部使用
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from app01.models import Book
from app01.ser import BookSerializer
class Book2View(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'price')
    
# urls.py
path('books2/', views.Book2View.as_view()),
]

# 使用：
http://127.0.0.1:8000/books2/?ordering=-price
http://127.0.0.1:8000/books2/?ordering=price
http://127.0.0.1:8000/books2/?ordering=-id
```



## 5 异常处理

```python
#统一接口返回

# 自定义异常方法，替换掉全局
# 写一个方法
# 自定义异常处理的方法
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
def my_exception_handler(exc, context):
    response=exception_handler(exc, context)
    # 两种情况，一个是None，drf没有处理
    #response对象，django处理了，但是处理的不符合咱们的要求
    # print(type(exc))

    if not response:
        if isinstance(exc, ZeroDivisionError):
            return Response(data={'status': 777, 'msg': "除以0的错误" + str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'status':999,'msg':str(exc)},status=status.HTTP_400_BAD_REQUEST)
    else:
        # return response
        return Response(data={'status':888,'msg':response.data.get('detail')},status=status.HTTP_400_BAD_REQUEST)
    
# 全局配置setting.py
'EXCEPTION_HANDLER': 'app01.app_auth.my_exception_handler',

```



## 6 封装Response对象(重要)

```python
# 以后都用自己封装的
class APIResponse(Response):
    def __init__(self,code=100,msg='成功',data=None,status=None,headers=None,**kwargs):
        dic = {'code': code, 'msg': msg}
        if  data:
            dic = {'code': code, 'msg': msg,'data':data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status,headers=headers)
# 使用
return APIResponse(data={"name":'lqz'},token='dsafsdfa',aa='dsafdsafasfdee')
return APIResponse(data={"name":'lqz'})
return APIResponse(code='101',msg='错误',data={"name":'lqz'},token='dsafsdfa',aa='dsafdsafasfdee',header={})
```





# 补充

## 1 变量后直接加逗号

```python

a=(3,)
a=3,  # a是元组
print(type(a))
```



# 作业

## 1 视图类继承GenericAPIView，get方法，post方法，用的序列化类不一样

## 2 图书一堆关联表的增删查改写完book表，author表，authordetail表，publish表，中间表

## 3 过滤，排序，认证，权限，频率，异常处理