# coding:utf-8
import matplotlib.pyplot as plt
# plt.figure()，面向过程的画图方法
import random
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 数据准备
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]

x_ticks_label = ["11点{}分".format(i) for i in x];
y_ticks = range(40)

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制图形
plt.plot(x, y_shanghai, color='b', linestyle='-', label='上海')
plt.plot(x, y_beijing, color='r', linestyle='--', label='北京')
# 显示图例
plt.legend(loc=0)

# 修改x，y轴坐标刻度显示
plt.xticks(x[::5], x_ticks_label[::5])
plt.yticks(y_ticks[::5])

# 添加网格显示
plt.grid(True, linestyle='--', alpha=1)

# 添加描述信息
plt.xlabel("时间", fontsize=10)
plt.ylabel("温度", fontsize=10)
plt.title("中午11点0分到12点之间的温度变化图示", fontsize=20)

# 保存图像，需要放到show之前
plt.savefig("./figure_demo.png")

# 3.展示图形
plt.show()
