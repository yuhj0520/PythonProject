# TypeError：数字类型无法与字符串类型相加
1 +’2’

# ValueError：当字符串包含有非数字的值时，无法转成int类型
num = input(">>: ")  # 输入hello
int(num)

# NameError：引用了一个不存在的名字x
x

# IndexError：索引超出列表的限制
l = ['egon', 'aa']
l[3]

# KeyError：引用了一个不存在的key
dic = {'name': 'egon'}
dic['age']

# AttributeError：引用的属性不存在


class Foo:
    pass


Foo.x

# ZeroDivisionError：除数不能为0
1 / 0


# Python提供了一个断言语句assert expression，断定表达式expression成立，否则触发异常AssertionError，与raise-if-not的语义相同，如下

age 7= '18'

# 若表达式isinstance(age,int)返回值为False则触发异常AssertionError
assert isinstance(age, int)

# 等同于
if not isinstance(age, int):
    raise AssertionError
