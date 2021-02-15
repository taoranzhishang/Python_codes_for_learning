import threading
import time
import win32api  # 引用系统函数


class Mythread(threading.Thread):  # 继承threading.Thread
    def run(self):  # run重写，
        win32api.MessageBox(0, "你的账户很危险", "来自支付宝的问候", 6)


mythread = []  # 集合list
for i in range(5):
    t = Mythread()  # 初始化
    t.setDaemon(True)  # 后台线程，主线程不等后台线程，不等待直接结束
    t.start()
    mythread.append(t)  # 加入线程集合

# threading.Thread默认是前台进程，主进程必须等前台。
print("game over")
