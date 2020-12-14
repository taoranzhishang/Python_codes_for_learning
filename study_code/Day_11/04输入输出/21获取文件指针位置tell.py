# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    21获取文件指针位置tell.py
# @Time:    2020/12/14 0:07
# @Software:PyCharm
filePath = "D:\\code\\py\\study_code\\Day_11\\04输入输出\\text.txt"
file = open(filePath, 'r')
print(file.tell())  # 获取文件指针位置，此使为0
myStr = file.readline()  # 读取一行，遇到换行
print(len(myStr))  # 获取长度
print(file.tell())  # 文件指针自动移至下一行，此使为16 -> 15+"\n"
file.close()
