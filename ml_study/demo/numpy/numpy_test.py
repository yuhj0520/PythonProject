# coding:utf-8
import numpy as np
import random
import time

a = []
for i in range(10000000):
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
