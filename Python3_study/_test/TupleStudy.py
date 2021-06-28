# coding:utf-8
t = (1, 2)
print(t)
print(type(t))
t = (1, 2, 3)
print(t)
# 元组定义必须加,
t = (1)
print(t)
print(type(t))
t = (1,)
print(t)
print(type(t))
print(t[0])
# 元组为不可变类型
t = (1, 2, 3)
dle t[0] #报错
print(t)