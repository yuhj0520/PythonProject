from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    print('我是视图函数index')
    obj = HttpResponse('index')

    def render():
        print('内部的render')
        return HttpResponse("O98K")
    obj.render = render
    return obj

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
"""
csrf_protect  需要校验
    针对csrf_protect符合我们之前所学的装饰器的三种玩法
csrf_exempt   忽视校验
    针对csrf_exempt只能给dispatch方法加才有效
"""
# @csrf_exempt
# @csrf_protect
def transfer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        target_user = request.POST.get('target_user')
        money = request.POST.get('money')
        print('%s给%s转了%s元'%(username,target_user,money))
    return render(request,'transfer.html')



from django.views import View

# @method_decorator(csrf_protect,name='post')  # 针对csrf_protect 第二种方式可以
# @method_decorator(csrf_exempt,name='post')  # 针对csrf_exempt 第二种方式不可以
@method_decorator(csrf_exempt,name='dispatch')
class MyCsrfToken(View):
    # @method_decorator(csrf_protect)  # 针对csrf_protect 第三种方式可以
    # @method_decorator(csrf_exempt)  # 针对csrf_exempt 第三种方式可以
    def dispatch(self, request, *args, **kwargs):
        return super(MyCsrfToken, self).dispatch(request,*args,**kwargs)

    def get(self,request):
        return HttpResponse('get')

    # @method_decorator(csrf_protect)  # 针对csrf_protect 第一种方式可以
    # @method_decorator(csrf_exempt)  # 针对csrf_exempt 第一种方式不可以
    def post(self,request):
        return HttpResponse('post')











