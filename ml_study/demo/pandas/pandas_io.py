# coding:utf-8
import pandas as pd

# csv文件读写
csv_data = pd.read_csv('./stock_day.csv', usecols=['open', 'close'])
print('csv文件读取，读取指定列open及close，读取值为:\n{}'.format(csv_data.head()))
# 文件写入操作
csv_data.to_csv('./csv_save.csv', columns=['close'], index=False)
data = pd.read_csv('./csv_save.csv')
print('csv文件写入操作，读取值为:\n{}'.format(data.head()))

# hdf文件读写
day_close = pd.read_hdf('./day_close.h5')
print('hdf文件读取，读取值为:\n{}'.format(day_close.head()))
day_close.to_hdf('./hdf_save.h5', key='day_close')
data = pd.read_hdf('./hdf_save.h5', key='day_close')
# data = pd.read_hdf('./hdf_save.h5') # 可以不指定key
# data = pd.read_hdf('./hdf_save.h5', key = '1') # 若指定key，则必须与写入文件时的key相同，否则报错
print('hdf文件写入操作，读取值为:\n{}'.format(data.head()))

# json文件读写
json_data = pd.read_json('./Sarcasm_Headlines_Dataset.json', orient='records', lines=True)
print('json文件读取，读取值为:\n{}'.format(json_data.head()))
json_data.to_json('./json_save.json', orient='records', lines = True)
