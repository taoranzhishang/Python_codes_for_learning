import threading
import win32api


class MyThread(threading.Thread):
    def run(self):
        win32api.MessageBox(0, "You are so beautiful", "From a single dog", 0)


"""
每一次遍历都会join()等待，所以是逐个执行
"""
for i in range(5):
    t = MyThread()
    t.start()
    t.join()  # 主线程等待线程t执行完成，逐个执行，解决线程冲突
print("over")
