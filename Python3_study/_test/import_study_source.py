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
