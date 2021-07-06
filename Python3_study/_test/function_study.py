# coding:utf-8
print('--------------------作用域测试--------------------')
'''
内建函数locals()查看当前作用域的局部变量
内建函数globals()查看当前作用域的全局变量
'''


def func():
    x = 10
    # 函数内部locals()为局部变量
    # 函数内部globals()与函数外部globals()返回相同内容
    print(f'函数内部局部变量: {locals()}')
    print(f'函数内部全局变量: {globals()}')


# 函数外部locals()与globals()返回相同内容
print(f'函数外部局部变量: {locals()}')
print(f'函数外部全局变量: {globals()}')
func()

print('\n')
print('--------------------函数内部修改变量--------------------')
# 函数内部修改变量值，实际相当于重新定义一个局部变量
x = 1


def func():
    x = 2
    print(f'函数内部修改不可变类型x={x}')


func()
print(f'函数外部修改不可变类型x={x}')

x = [1, 2]
y = [1, 2]


def func():
    x = [3, 4]
    x.append(3)
    y.append(3)
    print(f'函数内部修改可变list类型x={x}')
    print(f'函数内部修改可变list类型y={y}')


func()
print(f'函数外部修改可变list类型x={x}')
print(f'函数外部修改可变list类型y={y}')

print('\n')
print('--------------------全局声明--------------------')
x = (1, 2)


def func():
    x = (3, 4)
    print(f'函数内部不可变tuple类型值x={x}')


func()
print(f'函数外部不可变tuple类型值x={x}')

x = (1, 2)


def func():
    '''
    global x = 10 提示语法错误
    global声明当前变量为全局变量，声明要与赋值分开处理
    当变量为不可变时，使用global可以修改全局变量的值
    '''
    global x
    x = (3, 4)
    print(f'局部变量: {locals()}')
    print(f'全局变量: {globals()}')
    print(f'函数内部不可变tuple类型值x={x}')


func()
print(f'函数外部不可变tuple类型值x={x}')

print('\n')
print('--------------------函数嵌套上级引用--------------------')


def func():
    x = 1
    print(f'内部变量修改前: {x}')

    def func1():
        '''
        nonlocal x = 10 提示语法错误
        nonlocal声明当前变量为外部嵌套的变量，声明要与赋值分开处理
        nonlocal声明会从当前函数的外层函数开始一层层去查找名字x，若是一直到最外层函数都找不到，则会抛出异常。
        '''
        nonlocal x
        # nonlocal y
        x = 2
    func1()
    print(f'内部变量修改后: {x}')


func()


print('--------------------函数对象--------------------')


def add(x, y):
    return x + y


# 1、函数赋值给一个引用
func = add
print(f'{func(1,2)}')

# 2、函数作为容器元素
map = {'a': add, 'b': max}
print(map)
print(map['a'](1, 2))
print(map.get('a')(1, 2))

# 3、函数作为函数的参数


def foo(x, y, paramater):
    return x + y + paramater(x, y)


print(foo(1, 2, func))

# 4、函数作为函数的返回值


def bar():
    return add


func = bar()
func(1, 2)


print('--------------------函数闭包closures--------------------')
'''
闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。
一般情况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。
'''

# 闭包函数，其中 exponent 称为自由变量


def nth_power(exponent):
    x = 'x'
    y = 'y'

    def exponent_of(base):
        x, y
        return base ** exponent
    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
print(f'计算 2 的平方:{square(2)},{nth_power(2)(2)}')  # 计算 2 的平方
print(f'计算 2 的立方:{cube(2)},{nth_power(3)(2)}')  # 计算 2 的立方
print(nth_power.__closure__)
print(square.__closure__)
print(square.__closure__[0].cell_contents, square.__closure__[
      1].cell_contents, square.__closure__[2].cell_contents)


'''
python中我们称上面的这个x,y为闭包函数exponent_of的一个自由变量(free variable)。
①闭包中的引用的自由变量只和具体的闭包有关联，闭包的每个实例引用的自由变量互不干扰。
②一个闭包实例对其自由变量的修改会被传递到下一次该闭包实例的调用。
'''


def outer_func():
    loc_list = []

    def inner_func(name):
        loc_list.append(len(loc_list) + 1)
        print('%s loc_list = %s' % (name, loc_list))
    return inner_func


test1 = outer_func()
test2 = outer_func()
test1('0')
test1('0')
test1('0')
test2('1')
test1('0')
test2('1')


print('\n--------------------函数不定长参数--------------------')
"""
*args与**kwargs，都可作为函数的形参，并且*与**后面的字母并不要求是这个关键字，
只有变量前面的*才是必须的，即*v、**vars也是可以的
当*args作为形参时，负责把多余的位置变量实参收集成元组，赋值给args
当**kwargs作为形参时，负责把多余的关键字变量实参收集成字典，赋值给kwargs
当*args作为实参时，负责把args变量对应的元组(或者列表、集合等)，打散成位置实参
当**kwargs作为实参时，负责把kwargs变量对应的字典，打散成关键字实参
因此函数定义时，参数顺序应该是
some_func(fargs, *args, **kwargs)
"""


def test_args_kwargs_argument(arg1, arg2, arg3):
    print(f"arg1:{arg1}, arg2:{arg2}, arg3:{arg3}")


def test_args_kwargs_parameter(arg1, *arg2, **arg3):
    print(f"arg1:{arg1}, arg2:{arg2}, arg3:{arg3}")


# *args及**kwargs作为实参
args = ("two", 3, 5)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
kwargs2 = {"x": 3, "y": "two", "z": 5}
# arg1:two, arg2:3, arg3:5
test_args_kwargs_argument(*args)
# arg1:5, arg2:two, arg3:3
test_args_kwargs_argument(**kwargs)
# arg1:1, arg2:(('two', 3, 5),), arg3:{'x': 1, 'y': '2'}
test_args_kwargs_parameter(1, args, x=1, y='2')
# arg1:two, arg2:(3, 5), arg3:{'x': 3, 'y': 'two', 'z': 5}
test_args_kwargs_parameter(*args, **kwargs2)
