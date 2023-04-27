# coding:utf-8
import pandas as pd

# 数据准备
data = pd.read_csv('./stock_day.csv')
data = data.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)

# 算数运算
print(f'DataFrame算数运算加法：{data["open"].add(10).head()}')
print(f'DataFrame算数运算减法：{data["open"].sub(10).head()}')
print(f'DataFrame算数运算减法：{data["open"].mul(10).head()}')
print(f'DataFrame算数运算除法：{data["open"].div(10).head()}')

# 逻辑运算
print('DataFrame逻辑运算，返回逻辑结果：\n{}'.format(data['open'] > 23))
print('DataFrame逻辑运算，返回满足逻辑条件的数据：\n{}'.format(data[data['open'] > 23].head()))
print('DataFrame逻辑运算函数，返回满足逻辑条件24>open>23的数据：\n{}'.format(data.query('open < 24 & open > 23').head()))
print('DataFrame逻辑运算函数，返回满足逻辑条件open in取值：\n{}'.format(data.query('open in (23.53, 23.85)')))

# 统计运算
print('DataFrame统计运算：综合分析\n{}'.format(data.describe()))
print('DataFrame统计运算：每列最大值\n{}'.format(data.max()))
print('DataFrame统计运算：每列最小值\n{}'.format(data.min()))
print('DataFrame统计运算：每列平均值\n{}'.format(data.mean()))
print('DataFrame统计运算：每列求和\n{}'.format(data.sum()))
print('DataFrame统计运算：每列标准差\n{}'.format(data.std()))
print('DataFrame统计运算：每列方差\n{}'.format(data.var()))
print('DataFrame统计运算：最大值索引\n{}'.format(data.idxmax()))
print('DataFrame统计运算：最小值索引\n{}'.format(data.idxmin()))

df = pd.DataFrame({'COL1': [2, 3, 4, 5, 4, 2],
                   'COL2': [0, 1, 2, 3, 4, 2]})
print('DataFrame统计运算：中位数\n{}'.format(df.median()))

# 累计统计函数
data = data.sort_index()
stock_rise = data['p_change']
print('DataFrame统计函数：计算前1/2/3/…/n个数的和\n{}'.format(stock_rise.head()))
import matplotlib.pyplot as plt

stock_rise.cumsum().plot()
plt.show()

# 自定义运算
print('DataFrame自定义函数，寻找open、close两列中，最大值与最小值的差值\n{}'.format(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)))
# 行axis=1
