# coding:'utf-8'
__all__ = ['x', 'get']
x = 1


def get():
    print(x)


def change():
    global x
    x = 0


class Foo:
    def func(self):
        print('from the func')

import os
file_name = os.path.basename(__file__)

if __name__ == '__main__':
    print(f'{file_name}被当做脚本执行, main')
else:
    print(f'{file_name}被当做模块执行, module')