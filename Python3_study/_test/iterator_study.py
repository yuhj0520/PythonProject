# coding:'utf-8'
# 迭代器
print('--------------------迭代器--------------------')
# 从语法形式上讲，内置有__iter__方法的对象都是可迭代对象，字符串、列表、元组、字典、集合、打开的文件都是可迭代对象
t = (1, 2, 3)  # 可迭代对象，不是迭代器，需要调用内置函数iter()，或者__iter__变成迭代器
print('123'.__iter__)  # str同上

print(iter(t))  # object内置对象iter，本质t.__iter__()，返回t的迭代器对象，后续可以用t进行next()操作
print(t.__iter__())
i = iter(t)
print(next(i))  # 本质就是在调用i.__next__()
print(i.__next__())
print(next(i))
# print(next(i))

'''
for循环在工作时，首先会调用可迭代对象goods内置的iter方法拿到一个迭代器对象，
然后再调用该迭代器对象的next方法将取到的值赋给item,
执行循环体完成一次循环，周而复始，直到捕捉StopIteration异常，结束迭代。
'''
goods = ['mac', 'lenovo', 'acer', 'dell', 'sony']
for item in goods:
    print(item)

'''
str对象不是一个迭代器，它是一个可迭代对象，而不是一个迭代器。
这意味着它支持迭代，但我们不能直接对其进行迭代操作。
使用内置函数，iter。它将根据一个可迭代对象返回一个迭代器对象。这里是我们如何使用它：
'''
my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))


print('\n--------------------生成器--------------------')
'''
生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环
yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，这个函数会返回一个迭代器对象
Python解释器会将其视为一个generator，如下示例调用fab(5)，不会执行fab函数，而是返回一个iterable对象
在for循环执行时，每次循环都会执行fab函数内部的代码，执行到 yield b 时，fab函数就返回一个迭代值(yeild后的值)，
并保存函数的运行状态挂起函数，下次迭代时，代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield b。
'''


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b      # 使用 yield
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)
f = fab(5)
print(next(f))


def foo():
    print("generator busi starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()  # 带有yield关键字的函数为生成器函数，在调用函数时，并不会执行函数，而是生成一个迭代器对象
print('实例化生成器对象后')
print(next(g))  # 开始调用生成器函数内部逻辑，遇到yield 4，不执行res的赋值操作，返回4，藉由print打印出来
print("*" * 20)
# 二次调用生成器函数内部逻辑，执行res赋值操作，由于yield 4在上一次循环过程中执行过，因此本次res赋值为None。
# 继续执行循环，再次遇到yield 4，不执行res的赋值操作，返回4，藉由print打印出来。
print(next(g))
print(g.send(2))  # 为防止上述情况，生成器函数send，可以将一个值传入到上次yield返回的位置，继续执行，并且send函数内部会调用next方法
print(g.send(None))  # 等同于next(g)
g.close()  # 提前关闭生成器
# print(next(g)) # error


print('\n--------------------生成式--------------------')
# 1、列表生成式
number_list = range(-5, 5)
# 类似filter list(filter(lambda x: x < 0, number_list))
trans_list = [x for x in number_list if x < 0]
print('list->', trans_list)

# 2、字典生成式
my_dict = {'1': '2', 'a': 'b', 'c': 'd'}
trans_dict = {k: v for k, v in my_dict.items() if k != '1'}
print('dict->', trans_dict)

# 3、集合生成式
my_set = {1, 2, 3, 4, 5}
trans_set = {x + 10 for x in my_set if x > 3}
print('set->', trans_set)

# 4、元祖生成器（非生成式）
my_tuple = tuple(range(-5, 5))
trans_tuple_generator = (x for x in range(-5, 5) if x > 0)
print('tuple->', trans_tuple_generator)
print('tuple->', trans_tuple_generator.__next__())
