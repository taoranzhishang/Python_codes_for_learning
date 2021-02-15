import threading
import time


def func1():
    e = threading.Event()  # 事件

    def func2():
        for i in range(10):
            e.wait()  # 等待
            e.clear()  # 重置等待，等待只会生效一次，所以需要重置等待
            print(i)

    threading.Thread(target=func2).start()  # 开启一个线程
    return e


t = func1()
for i in range(10):
    time.sleep(i)
    t.set()  # 通知
