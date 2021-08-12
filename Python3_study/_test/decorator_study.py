# coding:'utf-8'
'''
普通装饰器可以在不修改原文件的情况下，对原方法进行一定装饰，
比如原方法在一个单独文件中，可以引入该模块的方法，并在当前作用域加以修改，不会影响其他引用该方法的程序
装饰器与切面，带注释的方法与类，可以理解为加入该切面的方法与类。
'''

# 1、普通装饰器
import time


def index(x, y, z):
    time.sleep(1)
    print('index %s %s %s' % (x, y, z))


def outter(func):
    # func = index的内存地址
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # index的内存地址()
        stop = time.time()
        print(stop - start)
    return wrapper


index = outter(index)  # index=wrapper的内存地址
index(1, 2, 3)

# 2、注释语法 @后面当做一个整体


def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()
# outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

print(a_function_requiring_decoration.__name__)
print(a_function_requiring_decoration.__closure__)
print(a_function_requiring_decoration.__closure__[0].cell_contents)


# 3、标准装饰器模板
def decorator_name(func):
    from functools import wraps

    @wraps(func)
    # 此注解作用是将代理的方法模拟成被装饰的方法，一些基本参数与被装饰的方法一致
    # 若不加此注解，那么在调用func.__name__时会返回decorated
    def decorated(*args, **kwargs):
        if not can_run:
            return "function can not run."
        return func(*args, **kwargs)
    return decorated


@decorator_name  # func = decorator_name(func)
def func():
    return("function can run")


can_run = True
print(func())

can_run = False
print(func())
print(func.__name__)


# 4、带参数的装饰器，在模板基础上，再包一层，最外层用于接收除装饰函数的其他参数
def logit(logfile='out.log'):
    from functools import wraps

    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容，a模式文件不存在创建文件并打开，文件存在打开文件指针移到文件末尾
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
        
    return logging_decorator


@logit()  # myfunc1 = (logit())(myfunc1)
def myfunc1():
    pass
# myfunc1 = (logit())(myfunc1)


# @logit(logfile='func2.log')  # myfunc2 = (logit(logfile='func2.log'))(myfunc2)
def myfunc2():
    pass


myfunc1()
myfunc2()


# 5、类装饰器
from functools import wraps
class Logit_class(object):

    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
    # 判断对象是否为可调用对象可以用函数 callable
    # 一个类实例要变成一个可调用对象，只需要实现一个特殊方法__call__()
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print('Logit_class notify record log.')


# myfunc3 = (Logit_class())(myfunc3)
# instance = Logit_class()
# myfunc3 = instance(myfunc3)
# callable(instance) 为True
@Logit_class() # 由于Logit_class类实现了__call__方法，因此此类的实例变为可调用对象
def myfunc3():
    pass


myfunc3()


class Email_logit_class(Logit_class):
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        # todo ???
        super(Email_logit_class, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        print('Email_logit_class notify email.')


@Email_logit_class()
def myfunc4():
    pass


myfunc4()
