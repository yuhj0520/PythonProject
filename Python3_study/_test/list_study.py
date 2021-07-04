# coding:utf-8
# python之禅
# import this

print('--------------------插入测试--------------------')
l = ['a', 'c', 'b', 'x']
# 队尾插入元素
l.append('y')
print(l)
# 在具体位置插入元素
l.insert(0, '1')
print(l)
l.insert(-1, '2')
print(l)

print('--------------------删除测试--------------------')
# 默认删除队尾元素
var = l.pop()
print(var)
print(l)
# 删除指定位置元素
var = l.pop(1)
print(var)
print(l)
del l[0]
print(var)
print(l)
# 删除具体值
l.remove('x')
print(l)

print('--------------------排序测试--------------------')
l = ['a', 'c', 'b', '2']
# 反转顺序
l.reverse()
print(f'反转顺序结果: {l}')
# 临时排序
testSorted = sorted(l)
print(f'sorted临时排序结果: {testSorted}')
print('sorted排序后:', l)
# 排序
l.sort()
print('sort排序后:', l)
# 倒叙
l.sort(reverse=True)
print('sort倒序后:', l)

print('--------------------range--------------------')
# 前闭后开
for value in range(2, 5):
    print(value)
# 相当于range(0,5)
for value in range(5):
    print(value)

# 根据range函数创建数字列表
nums = list(range(5))
print(nums)

# range函数第三个参数含义为步长step
nums = list(range(1, 11, 2))
print(nums)

print('--------------------列表解析--------------------')
# 变量 = [含有变量的表达式 用于给变量赋值的for循环]
l = [value * 2 for value in range(1, 10, 2)]
print(l)

print('--------------------切片--------------------')
print(f'初始值:{l}')
# 列表[起始索引:终止索引:步长step]，前闭后开，返回值结果同为列表
print(l[1:3])
print(l[0:3])
print(l[:3])
print(l[1:])
print(l[:])
print(l[1::2])
print(type(l[1::2]))

print('--------------------使用切片克隆克隆--------------------')
print(f'初始值:{l},{id(l)}')
clone1 = l[:]
clone2 = l[::]
print(clone1, id(clone1))
print(clone1, id(clone2))
