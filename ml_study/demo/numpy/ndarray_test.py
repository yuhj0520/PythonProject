# coding:utf-8
import numpy as np

print('--------------------ndarray逻辑运算--------------------')
score = np.random.randint(40, 100, (3, 5))
print(f'生成随机[10,5]数组{score}')
print(f'数组中每个元素进行逻辑运算{score > 60}')

# score[score > 60] = 1
# print(f'数组中每个元素进行赋值操作{score}')

print(f'数组中每个元素是否都大于60{np.all(score > 60)}')
print(f'切片后数组中每个元素是否都大于60{np.all(score[0:2, :] > 60)}')
print(f'切片后数组中是否存在大于90的数据{np.any(score[0:2, :] > 90)}')

# 三元运算符np.where三元运算符返回新数组，logical_and逻辑和，logical_or逻辑与
print(
    f'数组中元素大于60小于90赋值1，否则为0{np.where(np.logical_and(score > 60, score < 90), 1, 0)}')

print('--------------------ndarray统计运算--------------------')
print('数组中最大值={}'.format(np.max(score)))
print('数组中最小值={}'.format(np.min(score)))
print('数组中平均值={}'.format(np.mean(score)))
print('数组中每列下标最大值={}'.format(np.max(score, axis=0)))
print('数组中每行下标最大值={}'.format(np.min(score, axis=1)))
print('数组中每列平均值={}'.format(np.mean(score, axis=0)))
print('数组中最大值对应的列下标值={}'.format(np.argmax(score, axis=0)))
print('数组中最小值对应的行下标值={}'.format(np.argmin(score, axis=1)))

print('--------------------数组间的运算--------------------')
# 数组与数运算
arr = np.array([[1, 2, 3], [5, 6, 1]])
print(f'原始数组={arr}')
print(f'每个元素+1，结果为{arr + 1}')
print(f'每个元素*3，结果为{arr * 3}')

a = np.array([1, 2, 3])
b = [1, 2, 3]
print(f'ndarry与原始数组区别，ndarray运算是针对每个元素进行{a * 2},原始数组针对整个数组进行运算{b * 2}')

# 数组与数组运算，数组在进行矢量化运算时，要求数组的形状是相等的，或者满足可朝某一方向扩展
arr1 = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr2 = np.array([[1], [3]])
print(f'数组1维度为{arr1.shape}')
print(f'数组2维度为{arr2.shape}')
print(f'两个数组维度满足广播机制，可以进行运算{arr1 * arr2}')

# 矩阵乘法
matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
matrixB = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 1]])
print(f'矩阵1维度为{matrixA.shape}')
print(f'矩阵2维度为{matrixB.shape}')
print(f'矩阵相乘={np.matmul(matrixA, matrixB)}')
print(f'矩阵相乘={np.dot(matrixA, matrixB)}')
# np.matmul中禁止矩阵与标量的乘法
print(f'矩阵与标量相乘={np.dot(matrixA, 10)}')
# print(f'矩阵与标量相乘={np.matmul(matrixA, 10)}')