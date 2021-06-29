# coding:utf-8
# 空元组
t = ()
print(t)
print(type(t))
t = (1, 2)
print(t)
print(type(t))
t = (1, 2, 3)
print(t)
# 元组定义必须加,
t = (1)
print(f'不加","定义后值为{t}')
print(f'不加","定义后类型为{type(t)}')
t = (1,)
print(f'加","定义后值为{t}')
print(f'加","定义后类型为{type(t)}')
print(t[0])
# 元组为不可变类型
t = (1, 2, 3)
# dle t[0] #报错
print(t)