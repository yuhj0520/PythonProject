# coding:utf-8
import numpy as np
import pandas as pd

print('--------------------pandas数据结构Series--------------------')
array = pd.Series(np.arange(0, 10))
print(array)

# 索引创建
array2 = pd.Series([1, 2, 3, 4, 5, 6], index=[2, 4, 6, 8, 10, 12])
print(array2)
# print(array2[0]) # 因定义时，指定了数组下标，因此会报数组越界错误
print(array2[2])

# 字典创建
array3 = pd.Series({"red": 10, "green": 20})
print(array3)

# Series属性
print('Series对象属性index为：{}'.format(array3.index))
print('Series对象属性values为：{}'.format(array3.values))
print('Series对象具体下标red值：{}'.format(array3['red']))
print('Series对象具体下标第一个下标值：{}'.format(array3[0]))

print('--------------------pandas数据结构DataFrame--------------------')
# 使用正态分布随机生成2行3列DataFrame数据
df1 = pd.DataFrame(np.random.randn(2, 3))
print(f'DataFrame随机生成数据：\n{df1}')

# 生成学生成绩，10个学生，5个学科（10行，5列）
score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
print(f'DataFrame生成学生原始数据：\n{score_df}')
# 添加行列索引名称
subjects = ["语文", "数学", "英语", "政治", "体育"]
students = ["同学" + str(i) for i in range(score_df.shape[0])]  # np对象的行索引
score_final = pd.DataFrame(score, index=students, columns=subjects)
print(f'DataFrame生成学生最终数据：\n{score_final}')

# DataFrame属性
print(f'DataFrame属性之索引：{score_final.shape}')
print(f'DataFrame属性之行索引：{score_final.index}')
print(f'DataFrame属性之列索引：{score_final.columns}')
print(f'DataFrame属性之具体值：\n{score_final.values}')
print(f'DataFrame属性之矩阵转置：\n{score_final.T}')
print(f'DataFrame属性之前2行数据：\n{score_final.head(2)}')  # 不加参数默认为5行
print(f'DataFrame属性之后3行数据：\n{score_final.tail(3)}')  # 不加参数默认为5行

students_2 = ["同学_" + str(i) for i in range(score_df.shape[0])]
score_final.index = students_2
print(f'DataFrame属性修改行索引后：\n{score_final}')
# score_final.index[3] = '学生_3' # 不可以单独设置某一具体索引下标
scroe_reset1 = score_final.reset_index()
scroe_reset2 = score_final.reset_index(drop=True)
print(f'DataFrame属性重置索引后：\n{scroe_reset1}')
print(f'DataFrame属性重置索引后：\n{scroe_reset2}')

# 以某列值设置为新的索引
df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
print(f'初始化DataFrame对象：\n{df}')
df1 = df.set_index('year')
df2 = df.set_index(['year', 'month'])
print(f'重新设置DataFrame索引，以year为新索引：\n{df1}')
print(f'重新设置DataFrame索引，以year,month为新索引：\n{df2}')

print('--------------------pandas数据结构MultiIndex--------------------')
print(f'MultiIndex：DataFrame使用多重索引：\n{df2.index}')
print(f'MultiIndex：names属性：\n{df2.index.names}')
print(f'MultiIndex：levels属性：\n{df2.index.levels}')
# MultiIndex对象创建
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
mi = pd.MultiIndex.from_arrays(arrays, names=("num", "col"))
print(f'MultiIndex：创建对象\n{mi}')
