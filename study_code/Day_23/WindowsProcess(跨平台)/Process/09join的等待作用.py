import os
import multiprocessing
import time


def func(str):
    print(__name__)
    print(str)
    print("ppid:", os.getppid())
    print("pid:", os.getpid())
    time.sleep(2)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=func, args=("p1",))
    p2 = multiprocessing.Process(target=func, args=("p2",))
    p3 = multiprocessing.Process(target=func, args=("p3",))
    """
    进程顺序执行，逐个，并发
    """
    # p1.start()  # 进程线程中的启动
    # p1.join()  # 等待
    # p2.start()
    # p2.join()
    # p3.start()
    # p3.join()
    """
    同时执行，乱序
    """
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
