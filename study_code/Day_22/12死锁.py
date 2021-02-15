import threading
import time
"""
死锁是两个锁调用时互相锁住没有解锁，导致下一个锁锁不住都在等待，需要调用完后解锁
"""
boyMutex = threading.Lock()  # 创建锁
girlMutex = threading.Lock()


class Boy(threading.Thread):
    def run(self):
        if boyMutex.acquire(1):  # 锁定成功继续往下执行
            print(self.name, "Boy say sorry start")
            time.sleep(3)
            # boyMutex.release()  # 释放锁，使下一个所能锁定成功
            if girlMutex.acquire(1):  # 锁定不成功，一直等待，死锁
                print(self.name, "Boy say sorry end")
                girlMutex.release()
            boyMutex.release()


class Girl(threading.Thread):
    def run(self):
        if girlMutex.acquire(1):  # 锁定成功继续往下执行
            print(self.name, "Girl say sorry start")
            time.sleep(3)
            # girlMutex.release()  # 释放锁，使下一个所能锁定成功
            if boyMutex.acquire(1):  # 锁定不成功，一直等待
                print(self.name, "Girl say sorry end")
                boyMutex.release()
            girlMutex.release()


# 开启2个线程
boy = Boy()
girl = Girl()
boy.start()
girl.start()
