import threading
import time

"""
兼顾线程同步、线程通信
"""


def func1():
    with cond:  # 使用条件变量，cond处于锁定状态，func2的cond处于等待
        for i in range(10):
            time.sleep(1)
            print(threading.current_thread().name, i)
            if i == 5:
                cond.wait()  # 等待，到5开始等待，此时func1释放cond，func2的cond锁定成功开始执行


def func2():
    with cond:
        for i in range(10):
            time.sleep(1)
            print(threading.current_thread().name, i)
        cond.notify()  # 通知，遍历完成后通知


cond = threading.Condition()  # 线程条件变量，func1、func2使用的是同一个变量，原理：一个在锁定使用另一个就等待
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
