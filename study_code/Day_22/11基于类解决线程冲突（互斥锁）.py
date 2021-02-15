import threading

num = 0
mutex = threading.Lock()

"""
5个线程同时随机执行，哪个先锁住执行哪个，其它的没锁柱，等待
"""
class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):  # 锁住成功执行下面代码，没有成功就一直等待，参数1代表独占
            for i in range(1000000):  # 锁住期间其它线程不能调用
                num += 1
            mutex.release()  # 释放锁
        print(num)


threadList = []
for i in range(5):
    t = MyThread()
    t.start()
    threadList.append(t)

for thd in threadList:
    thd.join()

print("over")
