# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    13文本读取英文.py
# @Time:    2020/12/13 22:33
# @Software:PyCharm
file = open(r"D:\code\py\study_code\Day_11\04输入输出\demo.txt", 'r')
myStr = file.read()  # 读取英文
print(myStr)
file.close()
