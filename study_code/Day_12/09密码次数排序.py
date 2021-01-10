# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    09密码次数排序.py
# @Time:    2021/1/9 13:45
# @Software:PyCharm
import operator

filepath = r"D:\code\py\study_code\Day_12\csdnpasswordtimes.txt"
file = open(filepath, "rb")
csdnpasswordtimes = file.readlines()
file.close()

newfile = []
for line in csdnpasswordtimes:
    line = line.decode("utf-8")
    line = line.split(' ')
    newfile.append(line)

# newfile.sort(key=operator.itemgetter(0))
newfile.sort(key=lambda x: int(x[0]))
newfile.reverse()

savingfilepath = r"D:\code\py\study_code\Day_12\csdnpasswordtimeslast.txt"
savingfile = open(savingfilepath, "wb")
for data in newfile:
    savingfile.write((data[0] + ' ' + data[1]).encode("utf-8"))
savingfile.close()
