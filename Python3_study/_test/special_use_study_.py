# coding:'utf-8'

# 1、三元表达式
# 如果条件为真，返回真 否则返回假
# condition_is_true if condition else condition_is_false
flag = '1'
flag_state = True if flag == '1' else False
print(f'三元表达式值为: {flag_state}')


# 2、lambda 参数:操作(参数)
# add = lambda x, y : x + y
# print(add(1, 2))

# 根据列表里每个值的key的第[1]个元素来进行排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]


# 3、内置函数:map。配合lambda表达式使用的函数map
# map(function_to_apply, list_of_inputs,...)
# function_to_apply映射函数，可为匿名函数
# list_of_inputs一个或多个序列
# 取参数2的迭代器，然后遍历迭代器中每个元素，按照参数1的函数映射进行处理，按照表达式组合成新的数据赋值给map对象
# 3.1 简单映射
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(f'map映射之后，列表求平方的范围值为: {squared}')


# 3.2 高级函数映射
def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]  # 包含两个函数引用的列表
for i in range(5):
    # 针对列表中每个函数，按照x(i)方式处理，即执行函数传入参数i，取得返回值，形成map对象
    value = map(lambda x: x(i), funcs)
    print(list(value))  # 将map对象转换成list

    # 类似三元表达式的列表生成式
    value2 = [x(i) for x in funcs]
    print(value2)


# 4、内置函数:filter。配合lambda表达式使用的函数filter
# filter(function_to_apply, list_of_inputs)，过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表。
# 取参数2的迭代器，然后遍历迭代器中每个元素，按照参数1的函数映射进行处理，过滤所有等于False的数据，留下所有等于True的数据，赋值给filter对象
number_list = range(-5, 5)
# 针对列表中每个数据，判断如果<0，那么留下该数据，最终组合成filter对象
less_than_zero = filter(lambda x: x < 0, number_list)
print('filter->', list(less_than_zero))  # 将filter对象转换成list

# 类似三元表达式的列表生成式
less_than_zero_2 = [x for x in number_list if x < 0]
print('filter->', less_than_zero_2)


# 5、内置函数:reduce。配合lambda表达式使用的函数reduce
from functools import reduce
# reduce(function, iterable[, initializer])
# function:有两个参数函数（可为匿名函数）、iterable:可迭代对象、initializer:可选，初始参数
# 针对列表中每个数据，取前两个值求乘积，结果作为新的x，取下一个值作为y，继续求乘积，直到迭代器中无数据。
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)


# 6、交换两个变量的值
a = 1
b = 2
print(f'交换两个变量的值，交换前，a={a}, b={b}')
a, b = b, a
print(f'交换两个变量的值，交换后，a={a}, b={b}')


# 7、函数文档注释
# 类与函数的文档注释要在类名下或者函数名下，多行用'''，单行用#
# 用help可以查看注释的文档内容


def test_help():
    '''This is test'''
    ...


help(test_help)
