# 元组就是"一个不可变的列表"
#1、作用：按照索引/位置存放多个值，只用于读不用于改

#2、定义:（）内用逗号分隔开多个任意类型的元素
# t=(1,1.3,'aa') # t=tuple((1,1.3,'aa'))
# print(t,type(t))


# x=(10) # 单独一个括号代表包含的意思
# print(x,type(x))

# t=(10,) # 如果元组中只有一个元素，必须加逗号
# print(t,type(t))

# t=(1,1.3,'aa') # t=(0->值1的内存地址,1->值1.3的内存地址,2->值'aaa.txt'的内存地址，)
# t[0]=11111

# t=(1,[11,22]) # t=(0->值1的内存地址,1->值[1,2]的内存地址，)
# print(id(t[0]),id(t[1]))
# # t[0]=111111111 # 不能改
# # t[1]=222222222 # 不能改
#
# t[1][0]=11111111111111111
# # print(t)
# print(id(t[0]),id(t[1]))


#3、类型转换
# print(tuple('hello'))
# print(tuple([1,2,3]))
# print(tuple({'a1':111,'a2':333}))

#4、内置方法
#优先掌握的操作：
#1、按索引取值(正向取+反向取)：只能取
# t=('aa','bbb','cc')
# print(t[0])
# print(t[-1])

#2、切片(顾头不顾尾，步长)
# t=('aa','bbb','cc','dd','eee')
# print(t[0:3])
# print(t[::-1])

#3、长度
# t=('aa','bbb','cc','dd','eee')
# print(len(t))
#4、成员运算in和not in
# print('aa' in t)

#5、循环
# for x in t:
#     print(x)

#6、
t=(2,3,111,111,111,111)
# print(t.index(111))
# print(t.index(1111111111))

print(t.count(111))