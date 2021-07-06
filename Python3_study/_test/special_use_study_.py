# coding:'utf-8'

# 三元表达式
# 如果条件为真，返回真 否则返回假
# condition_is_true if condition else condition_is_false
flag = '1'
flag_state = True if flag == '1' else False
print(f'三元表达式值为: {flag_state}')

# lambda 参数:操作(参数)
# add = lambda x, y : x + y
# print(add(1, 2))

# 根据列表里每个值的key的第[1]个元素来进行排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
