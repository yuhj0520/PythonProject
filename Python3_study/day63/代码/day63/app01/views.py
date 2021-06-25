from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View


class MyLogin(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        return HttpResponse('post请求')


def index(request):
    # 模版语法可以传递的后端python数据类型
    n = 123
    f = 11.11
    s = '我也想奔现'
    b = False
    l = ['小红','姗姗','花花','茹茹','敏敏','新新']
    t = (111,222,333,444)
    d = {'username':'jason','age':18,'info':'这个人有点意思','hobby':[111,222,333,{'info':'NB'}]}
    se = {'晶晶','洋洋','嘤嘤'}
    lll = []
    def func():
        print('我被执行了')
        return '你的另一半在等你'

    class MyClass(object):
        def get_self(self):
            return 'self'

        @staticmethod
        def get_func():
            return 'func'

        @classmethod
        def get_class(cls):
            return 'cls'

        # 对象被展示到html页面上 就类似于执行了打印操作也会触发__str__方法
        def __str__(self):
            return '到底会不会？'

    obj = MyClass()

    file_size = 123123112
    import datetime
    current_time = datetime.datetime.now()
    # return render(request,'index.html',{})  # 一个个传

    info = '本 文 始 发 于个 人公 众 号：Tec hFlo w，原创不易，求个关注 今天是LeetCode专题第41篇文章，我们一起来看一道经典的动态规划问题Edit Distance，编辑距离。 今天这道题我本来是想跳过的，因为它实在是太经典了，属于典型的老掉牙问题了。但是想了想，一方面因为之前立了flag要把所有Med ...'
    egl = 'my name is jason my age is 18 and i am from China'

    msg = 'I Love You And You?'
    hhh = '<h1>敏敏</h1>'
    sss = '<script>alert(123)</script>'

    from django.utils.safestring import mark_safe
    res = mark_safe('<h1>新新</h1>')
    return render(request,'index.html',locals())


def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'loginn.html')

def reg(request):
    return render(request,'reg.html')