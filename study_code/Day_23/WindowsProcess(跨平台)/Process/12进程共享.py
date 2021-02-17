import multiprocessing
import os

"""
全局变量在进程中数据是独立的，变量可以共享
"""
myList = []


def func():
    global myList
    myList.append(1)
    myList.append(2)
    myList.append(3)
    print(os.getpid(), myList)


if __name__ == "__main__":
    """
    子进程
    """
    p = multiprocessing.Process(target=func, args=())
    p.start()
    """
    主进程
    """
    myList.append('a')
    myList.append('b')
    myList.append('c')
    print(os.getpid(), myList)
