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
# data['open'] = 1
# data.close = 0
print(f'pandas赋值后数据为：\n{data}')

# 排序
sort_data1 = data.sort_values("open", ascending=True).head()
sort_data2 = data.sort_values("open", ascending=False).head()
print(f'DataFrame按照open列升序进行排序，结果为：\n{sort_data1}')
print(f'DataFrame按照open列降序进行排序，结果为：\n{sort_data2}')
print(f'DataFrame按照open，high列升序进行排序，结果为：\n{data.sort_values(by=["open","high"], ascending=True)}')
print(f'DataFrame按照索引值升序进行排序，结果为：\n{data.sort_index()}')


print(f'Series按照值升序进行排序，结果为：\n{data["high"].sort_values().head()}')
print(f'Series按照索引升序进行排序，结果为：\n{data["high"].sort_index().head()}')