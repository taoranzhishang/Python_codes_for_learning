# import os
# os.mkdir(r"C:\Users\Tsinghua-yincheng\Desktop\day13\split") #创建文件夹

"""
创建切割小文件
"""
num = 10
filesplitlist = []  # 文件集合
for i in range(num):
    filepath = r"C:\Users\Tsinghua-yincheng\Desktop\day13\split\data" + str(i + 1) + ".txt"
    file = open(filepath, "wb")
    filesplitlist.append(file)
"""
读取大文件
"""
fileallpath = r"C:\Users\Tsinghua-yincheng\Desktop\day13\bigdata.txt"  # 归并
fileall = open(fileallpath, "rb")  # 写入
i = 0
for line in fileall:
    filesplitlist[i % num].write(line)
    i += 1
    # print(line)
fileall.close()
for i in range(num):
    filesplitlist[i].close()  # 关闭文件
