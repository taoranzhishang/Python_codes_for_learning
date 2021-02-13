import threading
import time

sem = threading.Semaphore(5)  # 限制线程的最大数量为n个


def thd():
    with sem:  # 锁定数量
        for i in range(10):
            print(threading.current_thread().name, i)
            time.sleep(1)


for i in range(5):  # 创建5个线程
    threading.Thread(target=thd).start()
