import threading
import os
import time


def func():
    os.system("calc")


delayThread = threading.Timer(5, func)  # 创建延时线程，5秒后执行func
delayThread.start()  # 启动

# i = 1
# while True:
#     time.sleep(1)
#     print(i)
#     i += 1
