import multiprocessing

"""
管道双向既可写入也可取出，双向通信
队列单向写入，一头写入一头取出，子进程写入父进程读取，父进程写入子进程读取，单向通信
"""
queue = multiprocessing.Queue()  # 进程队列可以实现共享


def func(Fqueue):
    print(id(Fqueue))
    Fqueue.put([1, 2, 3, 4])  # 子进程写入


if __name__ == "__main__":
    print(id(queue))
    # queue.put(['a', 'b'])  # 队列只能单向写入，单向取出（只能有一处写入）
    p = multiprocessing.Process(target=func, args=(queue,))
    p.start()
    p.join()
    print(queue.get())  # 父进程取出
