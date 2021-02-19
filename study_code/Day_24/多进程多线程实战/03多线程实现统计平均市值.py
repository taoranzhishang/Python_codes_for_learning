import csv
import threading
import queue
import os


class getdatatotal(threading.Thread):
    def __init__(self, path, queue):
        threading.Thread.__init__(self)
        self.path = path
        self.queue = queue

    def run(self):
        print("start", self.getName())
        reader = csv.reader(open(self.path, "r"))  # 读取
        num = 0
        alldata = 0
        for item in reader:
            if num == 0:
                pass
            else:
                alldata += eval(item[13])  # 累加所有的市值

            num += 1

        print(alldata / num, self.getName())  # 计算结果
        self.queue.put(alldata / num)  # 保存结果到队列


myqueue = queue.Queue(0)  # 无限容量
path = "C:\\Users\\Tsinghua-yincheng\\Desktop\\day24\\csv"
filelist = os.listdir(path)
filepathlist = []
for filename in filelist:  # 形成完整路径
    filename = path + "\\" + filename
    filepathlist.append(filename)

threadlist = []
for path in filepathlist:
    mythread = getdatatotal(path, myqueue)
    mythread.start()
    threadlist.append(mythread)  # 创建线程加入列表
for thread in threadlist:
    thread.join()

while not myqueue.empty():
    data = myqueue.get()
    print(data)
