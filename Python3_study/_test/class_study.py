# coding:'utf-8'

# 类定义时，所有类都继承与object类，所以如下类在定义时，等同于class Game(object)


class Game:

    # 类的属性（成员变量），实例化后，对象会继承类定义的属性
    name = 'default_name'
    develop_time = '30d'

    # 类的方法
    # self只是约定的名称，类的方法第一个参数为self，作用类似this
    # 类的所有方法必须要有此参数，否则创建类实例时会报错
    def __init__(self, name, classification, price):
        # 修改的是实例对应的属性，不会影响其他实例的属性
        self.name = name
        self.classification = classification
        self.price = price
        self.startDate = '20210704'

    def game_info(this):
        print(f'Game info: name is "{this.name}" ,classification is '
              f'"{this.classification}", price is "{this.price}"')

    # 必须要显示指出self参数，否则类声明定义时不报错，但是调用方法时会报错
    def game_info_2():
        print(f'Game info: name is "name" ,classification is '
              f'"classification", price is "price"')


print(f'类名.__dict__用来查看这个类容器内盛放的东西{Game.__dict__}')
my_sweep = Game('sweep', 'D', '1$')
my_sweep.game_info()
my_sweep.develop_time = '20d'
# 必须要显示指出self参数，否则如果不加第一个参数会报错
# my_sweep.game_info_2()


class RpgGame(Game):

    def __init__(self, name, classification, price):
        super().__init__(name, classification, price)
        self.game_time = '100h'

    # 覆盖/重写，类没有重载，同名函数后面的会覆盖前面的
    def game_info(self):
        print(f'Game info: name is "{self.name}" ,'
              f'classification is "{self.classification}",'
              f'price is "{self.price}",'
              f'game time is "{self.game_time}"')


my_rpggame = RpgGame('Final Fantasy VII Remake', 'A', '70$')
my_rpggame.game_info()
print(f'my_sweep name is "{my_sweep.name}"')
print(f'my_sweep develop_time is "{my_sweep.develop_time}"')
print(f'RpgGame name is "{my_rpggame.name}"')
print(f'RpgGame develop_time is "{my_rpggame.develop_time}"')


print('\n--------------------类的私有变量--------------------')

'''
①、在Python中，没有绝对在外部访问不了的变量，私有化只是一个约定
②、以单个下划线开头的变量或方法应被视为非公开的API，外部的调用者也不应该去访问以单下划线开头的变量或方法
③、Python通过一个非常简单的机制完成了一个伪私有化功能，这个机制名叫名称转写(name mangling)：
    以双下划线开头，并以最多一个下划线结尾的标识符，例如__X，会被转写为_classname__X，其中classname为类名。
④、类的方法也与类的变量一样，__开头也会发生变形
⑤、变形操作只在类定义阶段发生一次，在类定义之后的赋值操作，不会变形
'''


class TestPrivate:
    _privateVar = '_varname'
    __privateVar = '_classname__varname'
    __privateVar_ = '_classname__varname_'
    __privateVar__ = '__varname__'


test = TestPrivate()
print(f'私有变量测试:_开头的变量，变量名不转换:{test._privateVar}')
# print(f'私有变量测试:__开头的变量:{test.__privateVar}') # 报错
print(f'私有变量测试:__开头的变量，变量名转换:{test._TestPrivate__privateVar}')
print(f'私有变量测试:__开头_结尾的变量，变量名转换:{test._TestPrivate__privateVar_}')
# print(f'私有变量测试:__开头__结尾的变量:{test._TestPrivate__privateVar__}') # 报错
print(f'私有变量测试:__开头__结尾的变量，变量名不转换:{test.__privateVar__}')
TestPrivate.__test = '__test'
print(f'私有变量测试:类定义之后的赋值操作，变量名不转换:{TestPrivate.__test}')


print('\n--------------------类的属性--------------------')
# Python专门提供了一个装饰器property，可以将类中的函数“伪装成”对象的数据属性，
# 对象在访问该特殊属性时会触发功能的执行，然后将返回值作为本次访问的结果


class Foo:
    def __init__(self, val):
        self.__NAME = val  # 将属性隐藏起来

    @property
    def name(self):
        return self.__NAME

    @name.setter  # 将name打上property标识后，才可以使用的方法，否则会报错
    def name(self, value):
        if not isinstance(value, str):  # 在设定值之前进行类型检查
            raise TypeError('%s must be str' % value)
        self.__NAME = value  # 通过类型检查后,将值value存放到真实的位置self.__NAME

    @name.deleter
    def name(self):
        # 主动抛出一个异常，相当于java的throw Exception
        raise PermissionError('Can not delete')


f = Foo('name')
print(f.name)
f.name = 'LiLi'  # 触发name.setter装饰器对应的函数name(f,’Egon')
print(f.name)
# f.name = 123  # 触发name.setter对应的的函数name(f,123),抛出异常TypeError
# del f.name  # 触发name.deleter对应的函数name(f),抛出异常PermissionError


print('\n--------------------类的继承--------------------')


# 类的属性或方法按照：对象本身->类Bar->父类Foo的顺序依次找下去
# 父类如果不想让子类覆盖自己的方法，可以采用双下划线开头的方式将方法设置为私有的（变形）
# python会在MRO列表（类名.mro()方法）上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止

# 多继承
class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')

    def test1(self):
        print('from C')


class D(B, C):
    pass


obj = D()
print(D.__base__)
obj.test()  # 结果为：from B
obj.test1()  # 结果为：from C
print(D.mro())  # 继承链
# mro列表检索规则
# 1.子类会先于父类被检查
# 2.多个父类会根据它们在列表中的顺序被检查
# 3.如果对下一个类存在两个合法的选择，选择第一个父类

# 1.由对象发起的属性查找，会从对象自身的属性里检索，没有则会按照对象的类.mro()规定的顺序依次找下去，
# 2.由类发起的属性查找，会按照当前类.mro()规定的顺序依次找下去，
# 3.super()严格来说，并不是到父类查找相应的属性或方法，而是沿着mro链来查找。因为python的多继承，即使没有继承关系，也可以沿着mro链向后继续查找。


class A:
    # A没有继承B
    def test(self):
        super().test()


class B:
    def test(self):
        print('from B')


class C(A, B):
    pass


obj = C()
print('super()按照mro链向后查找属性或方法')
obj.test()  # 属性查找的发起者是类C的对象obj，所以中途发生的属性查找都是参照C.mro()



print('\n--------------------类的多态--------------------')
# 借助abc模块实现抽象类的概念
from abc import ABCMeta, abstractmethod
class Task(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        print('抽象方法中实现会报错')  # 抽象方法中有具体实现不会报错，但无意义
        pass

# t = Task() # 抽象类实例化会报错


class SubTask(Task):
    def __init__(self):
        super().__init__()

    # 若不覆盖父类抽象方法，在类定义时不会报错，在类实例化时会报错
    def run(self):
        print('必须实现父类抽象方法')


st = SubTask()
st.run()


print('\n--------------------类的绑定方法与非绑定方法--------------------')
'''
1、在类中正常定义的方法默认是绑定到对象的。
2、在类的某个方法加上装饰器@classmethod后，该函数就绑定到了类，为类的方法。python中类本质上也是一个对象
2、在类中某个方法加上装饰器@staticmethod后，该函数就变成了非绑定方法，也称为python静态方法。
'''

class TestBind:
    str = 'test';

    def __init__(self):
        pass
    def get_str(self):
        return self.str;

    @classmethod
    def test_class_method(cls):
        return cls.str

    @staticmethod
    def test_static_method():
        print('static method')

tb1 = TestBind()
tb1.str = 'test_new'

print(f'类的属性值str值为:{TestBind.str}');
print(f'对象的属性值str值为:{tb1.get_str()}');
print(f'通过类名.classmethod方法获取的str值为:{TestBind.test_class_method()}');
print(f'通过对象名.classmethod方法获取的str值为:{tb1.test_class_method()}');

TestBind.test_static_method()
tb1.test_static_method()
class Foo:
    def __init__():
        pass
Foo.test_static_method();
