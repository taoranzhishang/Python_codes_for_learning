# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    20文件指针seek.py
# @Time:    2020/12/13 23:49
# @Software:PyCharm
filePath = "D:\\code\\py\\study_code\\Day_11\\04输入输出\\text.txt"
file = open(filePath, 'r')
"""
第一个参数表示偏移量，指针移动的字计数，第二个参数0表示文件开头，1表示当前位置，2表示文件末尾
不支持符偏移
"""
file.seek(15 + 1, 0)  # 从文件开头移到第15个字节位置，但是还有一个换行符所以加1
thisLine = file.readline()  # 文件指针移到第2行，读取的是第2行
# print(len(thisLine))
print(thisLine)

file.close()
