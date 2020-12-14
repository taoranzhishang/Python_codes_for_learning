# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    18文本读取若干方式.py
# @Time:    2020/12/13 23:24
# @Software:PyCharm
file = open(r"D:\code\py\study_code\Day_11\04输入输出\text.txt", 'r')
# print(file.read())#未加参数，默认读取全部
# print(file.read(1))#按个数读取字符，1个 N
# print(file.read(2))#2个 ev
"""
每次读取后，文件指针后移，读取数据会自动后移
"""
# print(file.readline(),end='')#读取一行，包括行尾的换行符，
# print(file.readline())
"""
读取后，文件指针后移
"""
myList = file.readlines()  # 读取全部，每一行字符串为列表的一个元素
print(myList)
file.close()
