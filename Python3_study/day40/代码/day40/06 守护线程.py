# from threading import Thread
# import time
#
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(1)
#     print('%s is over'%name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=task,args=('egon',))
#     t.daemon = True
#     t.start()
#     print('主')

"""
主线程运行结束之后不会立刻结束 会等待所有其他非守护线程结束才会结束
    因为主线程的结束意味着所在的进程的结束
"""


# 稍微有一点迷惑性的例子
from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print('end123')


def func():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=func)
    t1.daemon = True
    t1.start()
    t2.start()
    print('主.......')














