import threading
import os
import csv


class ReadLine(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path
        self.line = -1

    def run(self):
        reader = csv.reader(open(self.path, 'r'))
        lines = 0
        for item in reader:
            lines += 1
        self.line = lines
        print(self.getName(), self.line)


threadList = []
lineList = []
path = "D:\\code\\py\\study_code\\Day_23\\多线程实战\\csv"
fileList = os.listdir(path)
for file in fileList:
    absPath = path + "\\" + file
    thd = ReadLine(absPath)
    thd.start()
    threadList.append(thd)
for thd in threadList:
    thd.join()
    lineList.append(thd.line)
print(lineList)
