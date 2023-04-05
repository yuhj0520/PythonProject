# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import random
import time

a = []
for i in range(100000):
    a.append(random.random())

b = np.array(a)
# Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁的多。
time1 = time.process_time_ns()

sum1 = sum(a)

time2 = time.process_time_ns()

sum2 = np.sum(b)

time3 = time.process_time_ns()

print(time3 - time2)
print(time2 - time1)

# ndarray的使用
score = np.array(
    [[80, 89, 86, 67, 79],
     [78, 97, 89, 67, 81],
     [90, 94, 78, 67, 74],
     [91, 91, 90, 67, 69],
     [76, 87, 75, 67, 86],
     [70, 79, 84, 67, 84],
     [94, 92, 93, 67, 64],
     [86, 85, 83, 67, 80]])

print(score)
print(score.shape)  # 数组维度的元组（行，列）
print(score.ndim)  # 数组的维数
print(score.size)  # 数组元素数量
print(score.itemsize)  # 数组每个元素的大小（字节）
print(score.dtype)  # 数组元素类型

# 指定类型
arr = np.array(['python', 'tensorflow', 'scikit-learn', 'numpy'],
               dtype=np.string_)
print(arr)

print('--------------------生成数组--------------------')
# 1、生成0,1数组
arr1 = np.ones((4, 8), dtype=np.string_)
arr2 = np.ones_like(score)
np.zeros((4, 8))
np.zeros_like(arr2)
print(arr1)
print(arr2)

# 2、从现有数组生成新数组，深拷贝，浅拷贝
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array(a)  # 深拷贝
c = np.asarray(a)  # 浅拷贝
a[0, 0] = 100
print(f'数组a={a}，数组b={b}，数组c={c}')

# 3、生成等差数列
array = np.linspace(0, 100, 5)  # 从0开始，到100截止，生成共5个数
array2 = np.linspace(0, 100, 5,
                     False)  # 从0开始，到100截止，生成共5个数，不包含100（不指定False，默认为true）
print(f'指定数量等差数列={array}')
print(f'指定数量等差数列={array2}')

array = np.arange(0, 100, 5)  # 从0开始，到100截止，步长5，前闭后开
print(f'步长等差数列={array}')

array = np.logspace(0, 2, 5)  # 从10^0开始，到10^2截止，生成共5个数
print(f'等比数列={array}')

print('--------------------正态分布--------------------')
# 4.生成符合正态分布的随机数组
# x1 = np.random.normal(0, 1, 100000000)
#
# plt.figure(figsize=(20, 10), dpi=100)
#
# plt.hist(x1, 1000)
#
# plt.show()

print('--------------------均匀分布--------------------')
# 5.生成符合均匀分布的随机数组
# x2 = np.random.uniform(0, 1, 100000000)
#
# plt.hist(x2, 1000)
#
# plt.show()


print('--------------------数组基本操作--------------------')
# 6.数组切片，每个维度数组分别切片
stock_change = np.random.normal(0, 1, (4, 5))
print(f'随机生成数组4行5列为{stock_change}')
print(f'切片数组第1行第2-4个元素为{stock_change[0, 1:4]}')
print(f'切片数组第3行第2、4个元素为{stock_change[2, 1:4:2]}')

# 7.数组形状修改
print(f'数组维度为{stock_change.shape}')
change1 = stock_change.reshape([5,4]) #返回新数组
print(f'数组变更形状后，返回新数组{change1}')

change2 = stock_change.reshape([5,-1]) #若为-1，则表示交由系统计算
#change2 = stock_change.reshape([3,-1]) #系统无法整除的情况会报错
print(f'数组变更形状后，返回新数组{change2}')

stock_change.resize([10,2]) #修改原数组
print(f'数组变更形状后，原数组变为{stock_change}')

print(f'数组转置{stock_change.T}')

# 8.类型修改
print(f'数组类型修改{stock_change.astype(np.string_)}')

# 9.数组去重
temp = np.array([[1, 2, 3, 4],[3, 4, 5, 6]])
print(f'数组去重{np.unique(temp)}')