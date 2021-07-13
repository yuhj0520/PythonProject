# coding:'utf-8'
'''
首次导入模块会做三件事：
1、执行源文件代码
2、产生一个新的名称空间用于存放源文件执行过程中产生的名字
3、在当前执行文件所在的名称空间中得到一个名字，该名字指向新创建的模块名称空间，
若要引用模块名称空间中的名字，需要加上该前缀，如
import foo
a = foo.x 

导入模块建议顺序
1. python内置模块
2. 第三方模块
3. 自定义模块

也可以在函数内导入模块，对比在文件开头导入模块属于全局作用域，在函数内导入的模块则属于局部的作用域。
'''
import import_study_source as iss
print(iss.x)
iss.get()
iss.change()
iss.get()
foo = iss.Foo()
foo.func()

# 模块的编写者可以在自己的文件中定义__all__变量用来控制*代表的意思，不在__all__变量里的变量函数类，是无法被引用的
from import_study_source import *  # 此时的*只代表x和get

print(x)  # 可用
get()  # 可用
# change() #不可用
# Foo() #不可用

import sys
# 模块搜索路径，从左到右来查找模块对应的文件
sys.path.append(r'D:/')
print(sys.path)
print(sys.__name__)

'''
一个Python文件有两种用途，一种被当主程序/脚本执行，另一种被当模块导入，
为了区别同一个文件的不同用途，每个py文件都内置了__name__变量，
该变量在py文件被当做脚本执行时赋值为“__main__”,在py文件被当做模块导入时赋值为模块名
'''


import os
file_name = os.path.basename(__file__)

if __name__ == '__main__':
    print(f'{file_name}被当做脚本执行, main')
else:
    print(f'{file_name}被当做模块执行, module')
