import multiprocessing
import time
"""
多进程，并发乱序
多进程加锁，逐个，乱序
"""

def func(lock,num):
    with lock:
        time.sleep(1)
        print(num)


if __name__ == "__main__":
    # for i in range(10):
    #     """
    #     创建10多进程，并发乱序执行
    #     """
    #     multiprocessing.Process(target=func, args=(i,)).start()
    for i in range(10):
        lock = multiprocessing.RLock()#创建锁
        multiprocessing.Process(target=func, args=(lock, i)).start()
