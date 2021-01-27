# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    11文件写入英文.py
# @Time:    2020/12/13 1:37
# @Software:PyCharm

file = open(r"D:\code\py\study_code\Day_11\04输入输出\demo.txt", 'w')  # 以写的方式打开demo.txt,没有则新建
myStr = "Hello Python"
file.write(myStr)  # 往demo.txt中写入myStr，英文以ASCII自动编码
file.close()  # 关闭文件
