# coding:utf-8
import matplotlib.pyplot as plt
import random

# 数据准备
x = range(60)
y = [random.uniform(15,18) for i in x]

# 1.创建画布
plt.figure(figsize=(20,8), dpi=100)

# 2.绘制图形
plt.plot(x,y)

# 3.展示图形
plt.show()