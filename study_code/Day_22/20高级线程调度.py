import threading


# def func1():
#     with cond:  # 锁定，下面的代码继续执行
#         for i in range(0, 10, 2):
#             print(threading.current_thread().name, i)
#             cond.notify()  # 通知线程2，线程2开始执行
#             cond.wait()  # 线程1等待，线程1先锁定所以先等待线程2才能锁定成功
##执行完后仍处于等待
# def func2():
#     with cond:  # 线程1锁定，线程2等待
#         for i in range(1, 10, 2):
#             print(threading.current_thread().name, i)
#             cond.notify()  # 通知等待中的线程1开始执行
#             cond.wait()  # 线程2等待

def func1():
    with cond:  # 锁定，下面的代码继续执行
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            cond.wait()  # 线程1等待，线程1先锁定所以先等待线程2才能锁定成功
            cond.notify()  # 通知线程2，线程2开始执行


def func2():
    with cond:  # 线程1锁定，线程2等待
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            cond.notify()  # 通知等待中的线程1开始执行
            cond.wait()  # 线程2等待


cond = threading.Condition()
threading.Thread(target=func1).start()  # 先创建线程1，再创2
threading.Thread(target=func2).start()
