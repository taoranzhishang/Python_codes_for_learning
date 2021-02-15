import threading
import win32api


class MyThread(threading.Thread):
    def run(self):
        win32api.MessageBox(0, "You are so beautiful", "From a single dog", 0)


threadList = []
"""
遍历一次添加一次，然后再join()
5个线程同时随机地执行，join()的作用没有体现
"""
for i in range(5):
    t = MyThread()
    t.start()
    threadList.append(t)

for thd in threadList:  # thd是从列表里每次遍历的一个线程
    thd.join()  # 主线程等待线程thd执行完成，同时执行，不需要阻塞
print("over")
