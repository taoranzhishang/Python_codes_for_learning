import os
import multiprocessing  # 多进程，模块


def info(title):
    print(title)
    print(__name__)
    print("Father ppid", os.getppid())
    print("Self pid", os.getpid())


if __name__ == "__main__":
    info("zhi")
    p = multiprocessing.Process(target=info, args=("wu",))
    p.start()
    p.join()  # 等待，父进程必须等子进程执行完后，才能执行后续代码
    print("s")
