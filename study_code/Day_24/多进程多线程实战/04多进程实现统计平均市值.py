import csv
import multiprocessing
import os


def gettotoal(path, queue):
    reader = csv.reader(open(path, "r"))  # 读取
    num = 0
    alldata = 0
    for item in reader:
        if num == 0:
            pass
        else:
            alldata += eval(item[13])  # 累加所有的市值
        num += 1
    queue.put(alldata / num)


if __name__ == "__main__":
    queue = multiprocessing.Queue()  # 队列可以实现共享-单向
    path = "C:\\Users\\Tsinghua-yincheng\\Desktop\\day24\\csv"
    filelist = os.listdir(path)
    filepathlist = []
    for filename in filelist:  # 形成完整路径
        filename = path + "\\" + filename
        filepathlist.append(filename)

    processlist = []
    for filepath in filepathlist:
        p = multiprocessing.Process(target=gettotoal, args=(filepath, queue))
        p.start()
        processlist.append(p)  # 加入列表

    for process in processlist:
        process.join()

    while not queue.empty():  # 进程传递用队列
        data = queue.get()
        print(data)
