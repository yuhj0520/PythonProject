# coding:utf-8
import pandas as pd

data = pd.read_csv('./stock_day.csv')
print(f'读取csv文件，头5行数据为\n{data.head()}')
# 删除索引对应的列数据
data = data.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)
print(f'按列删除，删除索引对应的列数据后，结果为\n{data}')

# 索引操作，pandas的索引为先列后行
print(f'pandas索引，默认先列后行，第[2018-02-23][open]值为：\n{data["open"]["2018-02-23"]}')
print(f'pandas索引，loc先行后列，第[2018-02-23~2018-02-14][open]值为：\n{data.loc["2018-02-23":"2018-02-14"]["open"]}')
print(f'pandas索引，iloc为下标，前3行前5列值为：\n{data.iloc[:3, :5]}')

# 赋值操作，整行整列
data['open']=1
data.close=0
