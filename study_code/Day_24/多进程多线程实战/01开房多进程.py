import multiprocessing
import os


# 指定位置进行检索
def findkaifang(kaifanglist, istart, iend, searchstr, lastlist):
    for i in range(istart, iend):
        line = kaifanglist[i].decode("gbk", "ignore")  # 解码二进制
        if line.find(searchstr) != -1:  # 找到
            print(line)
            lastlist.append(line)  # 保存结果


def loaddata(kaifanglist):
    path = "Z:\\F\\第一阶段视频\\20170424\\vedio\\大数据相关数据\\kaifanglite.txt"
    file = open(path, "rb")
    kaifanglist.extend(file.readlines())  # 全部读入内存


if __name__ == "__main__":
    kaifanglist = multiprocessing.Manager().list()  # 主进程有一份,读取文件
    lastlist = multiprocessing.Manager().list()  # 保存结果
    loaddata(kaifanglist)
    lines = len(kaifanglist)  # 数据的长度
    N = 10  # 开启10个进程
    processlist = []  # 进程列表
    findstr = input("请输入要查询的人名")
    '''
     for i in range(0, N - 1):  # 0,1,2,3,4,5,6,7,8  数据切割
        process = multiprocessing.Process(target=findkaifang,
                                          args=(kaifanglist,
                                                i * (lines // (N - 1)),
                                                (i + 1) * (lines // (N - 1)),
                                                findstr,
                                                lastlist
                                                ))
        process.start()
        processlist.append(process)


    # 97 =  97//10*10=90
    mylastp = multiprocessing.Process(target=findkaifang,
                                          args=(kaifanglist,
                                                (lines//(N-1))*(N-1),
                                                lines,
                                                findstr,
                                                lastlist
                                                ))
    mylastp.start()
    processlist.append(mylastp)
    '''

    # 97 =  97//10*10=90
    mylastp = multiprocessing.Process(target=findkaifang,
                                      args=(kaifanglist,
                                            0,
                                            lines,
                                            findstr,
                                            lastlist
                                            ))
    mylastp.start()
    processlist.append(mylastp)

    for process in processlist:
        process.join()  # 主进程等待其他进程都干完活

    file = open("last.txt", "wb")  # 保存结果
    for line in lastlist:
        file.write(line.encode("utf-8"))
    file.close()
