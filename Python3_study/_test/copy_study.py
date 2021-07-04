# coding:utf-8
# l = [value * 2 for value in range(1, 10, 2)]
l = [
    'e',
    'lxx',
    [1, 2]
]
print('\n--------------------使用切片方式克隆(无法克隆列表中的可变对象)--------------------')
print(f'初始值:{l},{id(l)}')
clone1 = l[:]
clone2 = l[::]
print(f'切片克隆1:{clone1, id(clone1)}')
print(f'切片克隆2:{clone2, id(clone2)}')
print(f'切片克隆1里的可变对象:{clone1[2], id(clone1[2])}')
print(f'切片克隆2里的可变对象:{clone2[2], id(clone2[2])}')


print('\n--------------------使用copy方式克隆(浅克隆，无法克隆列表中的可变对象)--------------------')
print(f'初始值:{l},{id(l)}')
clone1 = l.copy()
clone2 = l.copy()
print(f'浅克隆1:{clone1, id(clone1)}')
print(f'浅克隆2:{clone2, id(clone2)}')
print(f'浅克隆1里的可变对象:{clone1[2], id(clone1[2])}')
print(f'浅克隆2里的可变对象:{clone2[2], id(clone2[2])}')

import copy
print('\n--------------------使用copy.deepcopy方式克隆(深克隆)--------------------')
print(f'初始值:{l},{id(l)}')
clone1 = copy.deepcopy(l)
clone2 = copy.deepcopy(l)
print(f'深克隆1:{clone1, id(clone1)}')
print(f'深克隆2:{clone2, id(clone2)}')
print(f'深克隆1里的可变对象:{clone1[2], id(clone1[2])}')
print(f'深克隆2里的可变对象:{clone2[2], id(clone2[2])}')
