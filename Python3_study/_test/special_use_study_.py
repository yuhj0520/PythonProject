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


# 3、配合lambda表达式使用的函数map
# map(function_to_apply, list_of_inputs)
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


funcs = [multiply, add] # 包含两个函数引用的列表
for i in range(5):
    value = map(lambda x: x(i), funcs) # 针对列表中每个函数，按照x(i)方式处理，即执行函数传入参数i，取得返回值，形成map对象
    print(list(value)) # 将map对象转换成list


# 4、配合lambda表达式使用的函数filter、reduce