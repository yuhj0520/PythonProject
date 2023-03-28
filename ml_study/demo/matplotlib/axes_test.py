# coding:utf-8
import matplotlib.pyplot as plt
# plt.figure()，面向过程的画图方法
import random
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 0.准备数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 5) for i in x]

x_ticks_label = ["11点{}分".format(i) for i in x];
y_ticks = range(40)

# 1.创建画布，1行，2列
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 2.绘制图像
axes[0].plot(x, y_shanghai, label="上海")
# axes[1].plot(x, y_beijing, color="r", linestyle="--", label="北京") #折线图
axes[1].scatter(x, y_beijing, color="r", linestyle="--", label="北京") #散点图

# 刻度显示
axes[0].set_xticks(x[::10])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::10])
axes[1].set_xticks(x[::10])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::10])

# 网格显示
axes[0].grid(True, linestyle='--', alpha=1)
axes[1].grid(True, linestyle='--', alpha=1)

# 描述信息
axes[0].set_xlabel('时间', fontsize=10)
axes[0].set_ylabel('温度', fontsize=10)
axes[0].set_title('中午11点0分到12点之间的温度变化图示', fontsize=20)
axes[1].set_xlabel('时间', fontsize=10)
axes[1].set_ylabel('温度', fontsize=10)
axes[1].set_title('中午11点0分到12点之间的温度变化图示', fontsize=20)

# 保存图像，需要放到show之前
plt.savefig("./axes_demo.png")

# 显示图例
axes[0].legend(loc=0)
axes[1].legend(loc=0)

# 3.图像显示
plt.show()
