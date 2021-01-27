import os

# os.listdir遍历所有文件或者文件夹。
# 返回list
# print(os.listdir(r"Z:\F\第一阶段视频\20170531\52G葫芦娃\163mail1\163mail1"))
"""
不用全部载入内存，两个遍历逐个写入
"""
filepath = r"Z:\F\第一阶段视频\20170531\52G葫芦娃\163mail1\163mail1"  # 路径
filelist = os.listdir(filepath)  # 返回list包含所有文件名
fileallpath = r"C:\Users\Tsinghua-yincheng\Desktop\day13\bigdata.txt"  # 归并
fileall = open(fileallpath, "wb")  # 写入
for filename in filelist:  # 循环每一个文件名
    filelitepath = filepath + "\\" + filename  # 路径
    print(filelitepath)  # 打印
    filer = open(filelitepath, "rb")  # 读取
    for line in filer:  # 每一行地区之后写入
        fileall.write(line)
    filer.close()  # 关闭
fileall.close()
