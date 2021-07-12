# coding:'utf-8'
# open返回的对象只能在with代码块内部使用，但with代码块内的变量，可以直接在代码块外部使用
with open('class_study.py',mode='rt',encoding='utf-8') as f:
    line = f.readline()
print(line)