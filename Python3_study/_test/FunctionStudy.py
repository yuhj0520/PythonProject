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
