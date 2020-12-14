# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    15读取错误.py
# @Time:    2020/12/13 22:45
# @Software:PyCharm
file = open(r"D:\code\py\study_code\Day_11\04输入输出\poetry.txt", "rb")
myStr = file.read()
print(myStr.decode("gbk", "ignore"))  # uft-8文本使用gbk编码读取，强行编码，ignore忽略错误
file.close()
