import threading

num = 0
mutex = threading.RLock()
"""
RLock()可以解决死锁问题，避免单线程死锁
"""


class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            num += 1
            print(self.name, num)

            if mutex.acquire(1):  # 直接锁不会成功，使用RLock
                num += 1000
                print(self.name, num)
                mutex.release()

            mutex.release()


for i in range(5):  # 开启5个线程
    t = MyThread()
    t.start()
