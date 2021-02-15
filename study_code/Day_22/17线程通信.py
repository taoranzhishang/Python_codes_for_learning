import threading
import time

"""
线程同步：多个线程的执行随机，谁先抢到谁先执行
线程通信：多个线程的执行需要set来激发，可以控制执行顺序
"""


def func1():
    e = threading.Event()  # 事件

    def func2():
        e.wait()  # 等待，线程卡断状态，后续代码要set过后才会执行
        print("ZHI")

    threading.Thread(target=func2).start()  # 开启一个线程
    return e


t = func1()
time.sleep(3)
t.set()  # 激发事件
