# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    14文本读取中文.py
# @Time:    2020/12/13 22:36
# @Software:PyCharm
file = open(r"D:\code\py\study_code\Day_11\04输入输出\poetry.txt", "rb")  # 二进制读取
myStr = file.read()
print(type(myStr))  # 读取后是二进制编码,<class 'bytes'>
print(myStr.decode("utf-8"))  # 中文使用utf-8，decode()转换二进制编码为文本
file.close()
