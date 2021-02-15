import threading
import time

num = 0  # 全局变量多个线程可以读写，传递数据
mutex = threading.Lock()  # 创建一个锁


class Mythread(threading.Thread):
    def run(self):
        global num
        with mutex:
            for i in range(1000000):  # 锁定期间，其他人不可以干活
                num += 1

        print(num)


mythread = []
for i in range(5):
    t = Mythread()
    t.start()
    mythread.append(t)
for t in mythread:
    t.join()
print("game over")

"""
   with mutex: 自动打开自动释放
            for i in range(1000000): #锁定期间，其他人不可以干活
                num+=1


    if mutex.acquire(1):#锁住成功继续干活，没有锁住成功就一直等待，1代表独占
            for i in range(1000000): #锁定期间，其他人不可以干活
                num+=1
            mutex.release() #释放锁
"""
