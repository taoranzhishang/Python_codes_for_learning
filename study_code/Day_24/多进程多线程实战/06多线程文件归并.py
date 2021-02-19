import csv
import threading


# 缓存，实时刷新，
# 线程提前，文件不等
def getlist(path):
    reader = csv.reader(open(path, "r"))  # 读取文件
    alllist = []
    for item in reader:  # 读取每一行
        alllist.append(item)  # 加入列表
    return alllist


def getfilelist(path):
    file = open(path, "rb")  # 读取文件
    alllist = file.readlines()
    return alllist


def thread1(alllist, csvw, e1, e2):
    for line in alllist:
        csvw.write(line)
        print(line.decode("gbk", "ignore"))
        e2.set()  # 通知e2干活
        e1.wait(10)  # e1接着等待
        e1.clear()


def thread2(alllist, csvw, e2, e3):
    for line in alllist:
        e2.wait(10)  # 等待e2开始干活
        csvw.write(line)
        print(line.decode("gbk", "ignore"))
        e2.clear()
        e3.set()  # 通知e3开始干活


def thread3(alllist, csvw, e3, e1):
    for line in alllist:
        e3.wait(10)  # 等待e3开始干活
        csvw.write(line)
        print(line.decode("gbk", "ignore"))
        e3.clear()
        e1.set()


# with open("1.csv","w",newline="") as  datacsv:
# csvw=csv.writer(open("xyz.csv","w",newline=""),dialect=("excel"))#最常用excel格式
file = open("xyz.txt", "wb")

e1 = threading.Event()  # 事件
e2 = threading.Event()  # 事件
e3 = threading.Event()  # 事件
mylist1 = getfilelist(r"C:\Users\Tsinghua-yincheng\Desktop\day24\csv\1.txt")
mylist2 = getfilelist(r"C:\Users\Tsinghua-yincheng\Desktop\day24\csv\2.txt")
mylist3 = getfilelist(r"C:\Users\Tsinghua-yincheng\Desktop\day24\csv\3.txt")
# print(mylist1)
# print(mylist2)
# print(mylist3)
myth1 = threading.Thread(target=thread1, args=(mylist1, file, e1, e2))
myth2 = threading.Thread(target=thread2, args=(mylist2, file, e2, e3))
myth3 = threading.Thread(target=thread3, args=(mylist3, file, e3, e1))
myth1.start()
myth2.start()
myth3.start()

myth1.join()
myth2.join()
myth3.join()

print("over")
file.close()
