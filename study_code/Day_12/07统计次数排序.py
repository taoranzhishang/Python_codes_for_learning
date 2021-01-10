# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    07统计次数排序.py
# @Time:    2021/1/9 12:49
# @Software:PyCharm
myList = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e']
length = len(myList)

i = 0
while i <= length - 1:  # i<length
    counter = 1  # 次数
    password = myList[i]
    while i + 1 <= length - 1 and myList[i] == myList[i + 1]:  # 首先保证i+1没有越界
        counter += 1  # 次数加1
        i += 1  # 下标前进
    else:
        print(password, counter)
        i += 1  # 在条件不满足时，下标前进
