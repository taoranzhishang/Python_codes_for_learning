import _thread  # 多线程
import time


def go():
    for i in range(10):  # 10秒
        print(i, "---------")
        time.sleep(1)


# for  i  in range(5): #50秒
#   go()
for i in range(5):  # 10秒
    _thread.start_new_thread(go, ())

for i in range(10):  # 10秒
    time.sleep(1)
print("game over")
