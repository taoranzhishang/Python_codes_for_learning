# "130402199208062724"

import threading
import os


class Find(threading.Thread):
    def __init__(self, kaifanglist, istart, iend, searchstr):
        threading.Thread.__init__(self)
        self.kaifanglist = kaifanglist  # 开放数据的内存地址
        self.istart = istart  # 开始的索引
        self.iend = iend  # 结束的索引
        self.seachstr = searchstr  # 需要搜索的数据

    def run(self):
        print(self.getName(), "start")
        for i in range(self.istart, self.iend):
            global isfind
            if isfind:  # 找到退出
                break
            line = self.kaifanglist[i].decode("gbk", "ignore")  # 读取一行
            if line.find(self.seachstr) != -1:
                print(self.getName(), line, end="")  # 搜索数据
                isfind = True
                break
        print(self.getName(), "end")


isfind = False
path = "Z:\\F\\第一阶段视频\\20170424\\vedio\\大数据相关数据\\kaifangX.txt"
file = open(path, "rb")
kaifanglist = file.readlines()  # 全部读入内存
lines = len(kaifanglist)  # 所有的行数
searchstr = input("输入要查询的数据")
N = 10  # 开启10个线程
threadlist = []
# 97 9    0-1000000  1000000-2000000  2000000-3000000
for i in range(0, N - 1):  # 0,1,2,3,4,5,6,7,8  数据切割
    mythd = Find(kaifanglist, i * (lines // (N - 1)), (i + 1) * (lines // (N - 1)), searchstr)
    mythd.start()
    threadlist.append(mythd)

# 97 =  97//10*10=90
mylastthd = Find(kaifanglist, lines // (N - 1) * (N - 1), lines, searchstr)
mylastthd.start()
threadlist.append(mylastthd)

for thd in threadlist:
    thd.join()
print("finish")

'''
path = "Z:\\F\\第一阶段视频\\20170424\\vedio\\大数据相关数据\\kaifangX.txt"
file = open(path, "rb")
kaifanglist = file.readlines()  # 全部读入内存
searchstr=input("输入要查询的数据")
finddata=Find(kaifanglist,0,len(kaifanglist),searchstr)
finddata.start()
finddata.join()
print("完工")
'''

# 路径
'''
path="Z:\\F\\第一阶段视频\\20170424\\vedio\\大数据相关数据\\kaifangX.txt"
file=open(path,"rb")
kaifanglist=file.readlines() #全部读入内存
searchstr=input("输入要查询的数据")
for  line  in kaifanglist:
    line=line.decode("gbk","ignore")
    if line.find(searchstr)!=-1:
        print(line)
'''

# "440102197103035617"
