# 昨日回顾

```python
# 1 请求和响应
# 2 请求 Request对象，drf新包装的，Request.data，Request.query_params, 重写了__getattr__,  request._request
# 3 json模块是否执行反序列化bytes格式
# 4 考你：视图类的方法中：self.request，就是当次请求的request

# 5 Response：类，实例化传一堆参，data=字典，status=状态码（有一堆常量），headers=响应头（字典），content_type=响应的编码方式
# 6 全局和局部配置，响应格式
# 7 drf默认配置文件，查找顺序--》先从类中属性找---》项目的setting找---》drf默认的配置找


# 8 视图家族
	-APIView---》继承自View
    -GenicAPIView---》APIView，做了一些扩展：
    	-queryset = None
    	-serializer_class = None
        -get_queryset()  经常用
        -get_serializer() 经常用
        -get_serializer_class() 内部来用，外部会重写
        -get_object()  经常用，获取一条数据（pk传过来）
        	-源码解析
            queryset = self.filter_queryset(self.get_queryset()) #返回所有数据queryset对象
            # lookup_url_kwarg就是pk，路由中有名分组分出来的pk
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            # {pk:4}  4 浏览器地址中要查询的id号http://127.0.0.1:8000/books6/4/
            filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
            # 根据pk=4去queryset中get单个对象
            obj = get_object_or_404(queryset, **filter_kwargs)
            self.check_object_permissions(self.request, obj)
            return obj
   -5 个视图扩展类（继承了object），每个里面写了一个方法（ListModelMixin：list方法）		
        ListModelMixin,
        CreateModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        RetrieveModelMixin
   -GenericAPIView的视图子类，9个，继承了GenicAPIView+一个或者两个或者三个视图扩展类
        CreateAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView,
        DestroyAPIView,
        ListCreateAPIView,
        RetrieveUpdateDestroyAPIView,
        RetrieveDestroyAPIView,
        RetrieveUpdateAPIView
  -视图集：ModelViewSet,ReadOnlyModelViewSet：继承了上面一堆（5个视图扩展和GenicAPIView）+自己写了一个ViewSetMixin（as_view方法），只要继承它的，路由得写成{‘get’：‘自己定义的方法’}
	-ViewSet=ViewSetMixin, views.APIView ：ViewSetMixin要放在前面
    -GenericViewSet=ViewSetMixin+GenicAPIView
    
    -ViewSetMixin（as_view方法）
    -ViewSetMixin+APIView=ViewSet
    -ViewSetMixin+GenicAPIView=GenericViewSet

```



# 今日内容

## 1 路由

```python
# 1 在urls.py中配置
    path('books4/', views.Book4View.as_view()),
    re_path('books4/(?P<pk>\d+)', views.Book4DetailView.as_view()),
# 2 一旦视图类，继承了ViewSetMixin，路由
	 path('books5/', views.Book5View.as_view(actions={'get':'list','post':'create'})), #当路径匹配，又是get请求，会执行Book5View的list方法
    re_path('books5/(?P<pk>\d+)', views.Book5View.as_view(actions={'get':'retrieve','put':'update','delete':'destroy'})),
 
# 3 继承自视图类，ModelViewSet的路由写法（自动生成路由）
	-urls.py
        # 第一步：导入routers模块
        from rest_framework import routers
        # 第二步：有两个类,实例化得到对象
        # routers.DefaultRouter 生成的路由更多
        # routers.SimpleRouter
        router=routers.DefaultRouter()
        # 第三步：注册
        # router.register('前缀','继承自ModelViewSet视图类','别名')
        router.register('books',views.BookViewSet) # 不要加斜杠了

        # 第四步
        # router.urls # 自动生成的路由,加入到原路由中
        # print(router.urls)
        # urlpatterns+=router.urls
        '''
	-views.py
		from rest_framework.viewsets import ModelViewSet
        from app01.models import Book
        from app01.ser import BookSerializer
        class BookViewSet(ModelViewSet):
            queryset =Book.objects
            serializer_class = BookSerializer
```

### 1.1 action的使用

```python
# action干什么用？为了给继承自ModelViewSet的视图类中定义的函数也添加路由
# 使用
class BookViewSet(ModelViewSet):
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    # methods第一个参数，传一个列表，列表中放请求方式，
    # ^books/get_1/$ [name='book-get-1'] 当向这个地址发送get请求，会执行下面的函数
    # detail：布尔类型 如果是True
    #^books/(?P<pk>[^/.]+)/get_1/$ [name='book-get-1']
    @action(methods=['GET','POST'],detail=True)
    def get_1(self,request,pk):
        print(pk)
        book=self.get_queryset()[:2]  # 从0开始截取一条
        ser=self.get_serializer(book,many=True)
        return Response(ser.data)
    
# 装饰器，放在被装饰的函数上方，method：请求方式，detail：是否带pk
```



## 2 认证

### 2.1 认证的写法

```python
# 认证的实现
	1 写一个类，继承BaseAuthentication，重写authenticate，认证的逻辑写在里面，认证通过，返回两个值，一个值最终给了Requet对象的user，认证失败，抛异常：APIException或者AuthenticationFailed
    2 全局使用，局部使用
```

### 2.2  认证的源码分析

```python
#1 APIVIew----》dispatch方法---》self.initial(request, *args, **kwargs)---->有认证，权限，频率
#2 只读认证源码： self.perform_authentication(request)
#3 self.perform_authentication(request)就一句话：request.user，需要去drf的Request对象中找user属性（方法） 
#4 Request类中的user方法，刚开始来，没有_user,走 self._authenticate()

#5 核心，就是Request类的 _authenticate(self):
    def _authenticate(self):
        # 遍历拿到一个个认证器，进行认证
        # self.authenticators配置的一堆认证类产生的认证类对象组成的 list
        #self.authenticators 你在视图类中配置的一个个的认证类：authentication_classes=[认证类1，认证类2]，对象的列表
        for authenticator in self.authenticators:
            try:
                # 认证器(对象)调用认证方法authenticate(认证类对象self, request请求对象)
                # 返回值：登陆的用户与认证的信息组成的 tuple
                # 该方法被try包裹，代表该方法会抛异常，抛异常就代表认证失败
                user_auth_tuple = authenticator.authenticate(self) #注意这self是request对象
            except exceptions.APIException:
                self._not_authenticated()
                raise

            # 返回值的处理
            if user_auth_tuple is not None:
                self._authenticator = authenticator
                # 如何有返回值，就将 登陆用户 与 登陆认证 分别保存到 request.user、request.auth
                self.user, self.auth = user_auth_tuple
                return
        # 如果返回值user_auth_tuple为空，代表认证通过，但是没有 登陆用户 与 登陆认证信息，代表游客
        self._not_authenticated()
```

### 2.3 认证组件的使用

```python
# 写一个认证类 app_auth.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01.models import UserToken
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 认证逻辑，如果认证通过，返回两个值
        #如果认证失败，抛出AuthenticationFailed异常
        token=request.GET.get('token')
        if  token:
            user_token=UserToken.objects.filter(token=token).first()
            # 认证通过
            if user_token:
                return user_token.user,token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求地址中需要携带token')

# 可以有多个认证，从左到右依次执行
# 全局使用，在setting.py中配置
REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":["app01.app_auth.MyAuthentication",]
}
# 局部使用，在视图类上写
authentication_classes=[MyAuthentication]
# 局部禁用
authentication_classes=[]
```







# 作业

## 1 继承ModelViewSet，获取所有的，只获取前10条

## 2 登陆接口，查询图书接口，必须登录后才能查看，token信息放在头里（认证组件），全局使用，局部禁用（login禁用）

## 3 使用simplerouter自动生成路由

