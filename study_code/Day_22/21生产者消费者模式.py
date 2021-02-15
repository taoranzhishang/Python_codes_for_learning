import threading
import queue
import time
import random

"""
生产者消费者模式就是队列中有生产者不生产，消费者可以获取，队列中没有生产者生产，消费者不会获取
"""


class CreatorThread(threading.Thread):
    def __init__(self, index, myQueue):
        threading.Thread.__init__(self)
        self.index = index
        self.myQueue = myQueue

    def run(self):
        while True:
            time.sleep(3)
            num = random.randint(1, 10000)
            self.myQueue.put("input 生产者" + str(self.index) + "蛋糕" + str(num))
            print("input 生产者" + str(self.index) + "蛋糕" + str(num))
        self.myQueue.task_done()  # 完成任务


class ConsumerThread(threading.Thread):
    def __init__(self, index, myQueue):
        threading.Thread.__init__(self)
        self.index = index
        self.myQueue = myQueue

    def run(self):
        while True:
            time.sleep(1)
            item = self.myQueue.get()
            if item == None:
                break
            print("客户", self.index, "买到物品", item)
        self.myQueue.task_done()


myQueue = queue.Queue(10)  # 队列。容量10，0代表无限容量
for i in range(3):
    CreatorThread(i, myQueue).start()
for i in range(8):
    ConsumerThread(i, myQueue).start()
