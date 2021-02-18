import multiprocessing
import os
import csv


def getLines(path):
    fileList = csv.reader(open(path, 'r'))
    lines = -1
    for file in fileList:
        lines += 1
    print(os.getpid(), lines)


if __name__ == "__main__":
    path = "D:\\code\\py\\study_code\\Day_23\\多线程实战\\csv"
    fileList = os.listdir(path)
    processList = []
    myList = multiprocessing.Manager().list()
    for file in fileList:
        absPath = path + "\\" + file
        p = multiprocessing.Process(target=getLines, args=(absPath,))
        p.start()
        processList.append(p)
    for process in processList:
        process.join()
