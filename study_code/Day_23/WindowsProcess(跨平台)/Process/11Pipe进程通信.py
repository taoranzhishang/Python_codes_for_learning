import multiprocessing
import os

"""
进程通信包含进程共享
"""


def func(conn):  # conn管道类型
    conn.send(['a', 'b', 'c', 'd'])  # 发送的数据
    print(os.getpid(), "conn", conn.recv())  # 收到的数据
    conn.close()


if __name__ == "__main__":
    conn1, conn2 = multiprocessing.Pipe()  # 创建一个管道，两个口
    print(id(conn1), type(conn1))  # 2995265805184 <class 'multiprocessing.connection.PipeConnection'>
    print(id(conn2), type(conn2))  # 2995317991840 <class 'multiprocessing.connection.PipeConnection'>
    p = multiprocessing.Process(target=func, args=(conn1,))  # 子进程
    p.start()
    conn2.send([1, 2, 3, 4])  # 主进程
    print(os.getpid(), "conn2", conn2.recv())
    p.join()
