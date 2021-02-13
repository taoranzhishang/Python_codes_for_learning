import time
import threading

"""
为了合理利用资源
"""
bar = threading.Barrier(3)  # 必须凑满n个才执行，多了少了一直等待，不往下执行


def thd():
    print(threading.current_thread().name, "start")
    time.sleep(5)
    bar.wait()
    print(threading.current_thread().name, "end")


for i in range(5):  # 创建5个线程
    threading.Thread(target=thd).start()
