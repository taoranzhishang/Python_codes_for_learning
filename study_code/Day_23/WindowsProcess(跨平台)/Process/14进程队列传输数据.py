import multiprocessing
import os

queue = multiprocessing.Queue()


def func(queue, num):
    queue.put(num)  # 传入数据
    print("put:", os.getppid(), os.getpid(), num)


if __name__ == "__main__":
    myList = []
    for i in range(10):
        p = multiprocessing.Process(target=func, args=(queue, i))
        p.start()
        myList.append(queue.get())  # 获取数据
    print(myList)
