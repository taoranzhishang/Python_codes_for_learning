# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    03字符串切割.py
# @Time:    2020/12/14 19:53
# @Software:PyCharm
str = "陶然至上 # 123456 # taoranzhishang@hotmail.com"
myList = str.split(" # ")  # split()的返回值是列表：['陶然至上', '123456', 'taoranzhishang@hotmail.com']
print(myList)  # 输出列表
print(myList[2])  # 输出索引为2的列表元素
