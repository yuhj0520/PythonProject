# coding:utf-8
print('--------------------集合基本操作--------------------')
# 类型转换
print(set([1, 2]))
print(set({'k1': 1, 'k2': 2}))

# {}为空字典，set()为空集合
s = set()
print(s, type(s))
# 添加元素add，集合无序、值不重复、集合内元素必须为不可变类型
s.add(1)
s.add('2')
s.add('2')
s.add((1, 2))
# s.add({}) 报错
print(s)

# 删除元素discard，remove
s.discard(1)
print(f'discard(1)后s={s}')
s.discard(2) # 元素不存在，discard不报错
print(f'discard(2)后s={s}')
s.remove('2')
print(f"remove('2')后s={s}")
# s.remove('3') # 元素不存在，remove报错

s = {1, (1, 2), '2'}
# pop 元素无序，随机删除一个元素，并返回该元素值
value=s.pop()
print(f'随机删除一个元素{value}')
print(f'随机删除一个元素后s={s}')

# update 一次性添加多个元素
s.update({1,3,5})
print(f'update添加元素后s={s}')

print('\n--------------------集合运算--------------------')
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
# 交集
print(f'交集{s1 & s2}')
print(f'交集{s1.intersection(s2)}')

# 并集
print(f'并集{s1 | s2}')
print(f'并集{s1.union(s2)}')

# 差集
print(f'差集{s1 - s2}')
print(f'差集{s1.difference(s2)}')

# 抑或，交集取反
print(f'抑或{s1 ^ s2}')
print(f'抑或{s1.symmetric_difference(s2)}')

# 包含
s1={1,2,3}
s2={1,2}
print(f's1包含s2:{s1 > s2}') # 当s1大于或等于s2时，才能说是s1是s2他爹
print(f's1是s2的父集合:{s1.issuperset(s2)}')
print(f's2是s1的子集合:{s2.issubset(s1)}') # s2 < s2  =>True