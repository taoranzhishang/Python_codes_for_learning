# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    22对象文件读写.py
# @Time:    2020/12/14 0:17
# @Software:PyCharm
"""
数据结构与文件的交互
"""
import pickle

"""
写入文件
"""
myList = [[1, 2, 3, 4, 5, 6], ["abc", "xyz", "你好天朝"]]
file = open(r"D:\code\py\study_code\Day_11\04输入输出\myList.bin", "wb")
pickle.dump(myList, file)  # 保存myLIst数据到file文件
file.close()

"""
读取文件
"""
# newList=[]
newFile = open(r"D:\code\py\study_code\Day_11\04输入输出\myList.bin", "rb")
newList = pickle.load(newFile)  # 读取文件到newList
print(newList)
