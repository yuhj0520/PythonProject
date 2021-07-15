# coding:'utf-8'
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


# 标准装饰器模板
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
