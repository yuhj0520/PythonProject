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


print('\n--------------------类的其他用法--------------------')
print(f'类名.__dict__用来查看这个类容器内盛放的东西{Game.__dict__}')
