import threading
import win32api

"""
基于类实现多线程，遍历一次实例化一次，启动一次
5个线程同时随机地执行
"""
class MyThread(threading.Thread):
    def run(self):  # 重写
        win32api.MessageBox(0, "You are so beautiful", "From a single dog", 0)


for i in range(5):
    t = MyThread()  # 实例化
    t.start()  # 开启

while True:
    pass
