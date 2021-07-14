# coding:utf-8
# 空列表
m = {}
print(type(m))
# 空集合
s = set({})
print(s)
print(type(s))
s.add(1)
print(s)

print('--------------------新建字典测试--------------------')
# 新建字典
m = {}
m['a'] = 1
m[(1, 2)] = 2
print(f'新建字典方式一：空字典添加数据，结果为：{m}')

m = {'a': '1', 'b': 2, 'b': {1: 2}, (1, 2): {1, 2}, }
print(f'新建字典方式二：直接赋值，结果为：{m}')

# 这种方式key值貌似只能是字符类型
m = dict(a=1, t={2})
print(f'新建字典方式三：对象方法，结果为：{m}')

# 这种方式key值貌似只能是字符类型
m = {}.fromkeys((1, 2, 3))
print(f'新建字典方式四：dict.fromkeys(list/set/tuple,None)，结果为：{m}')
m = {}.fromkeys({1, 2, 3}, 'defaultValue')
print(f'新建字典方式四：dict.fromkeys(list/set/tuple,value)，结果为：{m}')


print('\n')
print('--------------------字典元素测试--------------------')
'''
key必须是不可变类型，字典key相同，后面覆盖前面 
value可以使任意类型
'''
m = {'a': '1', 'b': 2, 'b': {1: 2}, (1, 2): {1, 2}, }
print(m)

# 循环默认为keys，可以有keys()、values()、items()分别获取关键字、值、元素，每个方法都返回特殊列表，可转换为list
for key in m:
    print(f'字典每个元素key :{key}')

for value in m.values():
    print(f'字典每个元素value :{value}')

for k, v in m.items():
    print(f'字典元素 :{k},{v}')

print(m.keys())
print(m.values())
print(m.items())

l = list(m.keys())
print(f'字典keys返回特殊类型列表，可以通过list转换成标准列表形式: {type(l),l}')


print('\n')
print('--------------------字典常用操作测试--------------------')
print(f'字典原始值为: {m}')
name = 'a'
print(m[name])
print(name in m)
# 以key为依据来删除
del m[name]
print(f'删除key=\'{name}\'后字典值为: {m}')

# pop删除：根据key删除元素，返回删除key对应的那个value值
popResult = m.pop('b')
print(popResult)
print(f'删除key=\'b\'后字典值为: {m}')
# pop的key不可以为不存在的key
# popResult = m.pop('a') 报错

# popitem删除：删除最后一个键值对，返回元组(删除的key,删除的value)
m = {'a': '1', 'b': 2, (1, 2): {1, 2}, 'b': {1: 2}, }
popResult = m.popitem()
print(popResult)
print(f'popitem删除后字典值为: {m}')

# clear清空
m.clear()
print(f'清空后字典值为: {m}')

# update 更新某个具体key对应的value，同时如果key不存在，则添加这个键值对
m = {'a': '1', 'b': 2, (1, 2): {1, 2}, 'b': {1: 2}, }
m.update({'a': 2, 'c': '3'})
print(f'更新后字典值为: {m}')

# get(k,default)取值，兼容性较好，如果key不存在，返回None，不会报错，同时
print(f'字典中get存在的key值为: {m.get("a")}')
print(f'字典中get不存在的key值为: {m.get("1")}')
print(f'字典中get不存在的key值，可以设置默认值: {m.get("1","default")}')
# v = m['1'] key不存在，报错

# setdefault设置key值，若key存在不更新value，若key不存在，添加kv到字典中
m = {}
m.setdefault('a', '1')
print(f'{m}')
m.setdefault('a', '2')
print(f'{m}')


print('\n')
print('--------------------字典有序测试--------------------')
# 字典实际为无序，但字典大部分操作会遵循字典中数据插入的顺序来进行处理
m1 = {'a': '1', 'b': 2, (1, 2): {1, 2}, 'b': {1: 2}, }
m2 = {'b': 2, 'a': '1', (1, 2): {1, 2}, 'b': {1: 2}, }
print(f'字典m1: {m1}')
print(f'字典m2: {m2}')
print(f'字典m1与m2顺序不同，但值相同m1==m2为{m1==m2}')

from collections import OrderedDict
m1 = OrderedDict()
m1[1] = 'a'
m1[2] = 'b'
m2 = OrderedDict()
m2[2] = 'b'
m2[1] = 'a'
print(f'OrderedDict有序字典m1: {m1}')
print(f'OrderedDict有序字典m2: {m2}')
print(f'字典m1与m2顺序不同，且值不相同m1==m2为{m1==m2}')