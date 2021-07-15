# coding:'utf-8'
# open返回的对象只能在with代码块内部使用，但with代码块内的变量，可以直接在代码块外部使用
with open('class_study.py', mode='rt', encoding='utf-8') as f:
    line = f.readline()
print(line)

# f.seek(n,模式):n指的是移动的字节个数
# 模式：
# 模式0：参照物是文件开头位置
# f.seek(9,0)
# f.seek(3,0) # 指针位置3

# 模式1：参照物是当前指针所在位置
# f.seek(9,1)
# f.seek(3,1) # 指针位置12

# 模式2：参照物是文件末尾位置，应该倒着移动
# f.seek(-9,2) # 3
# f.seek(-3,2) # 9

import json  # 不是所有格式都可以读取
with open('file_study_content.json', mode='rt', encoding='utf-8') as f:
    line = json.load(f)
print(line)


try:
    with open(r'd:\file_study_content.json', mode='rt', encoding='utf-8') as f:
        line = json.load(f)
except:
    with open(r'd:\file_study_content.json', mode='wt', encoding='utf-8') as f:
        json.dump(line, f)
print(line)
