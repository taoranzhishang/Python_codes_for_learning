# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    18列表生成式.py
# @Time:    2020/12/12 17:25
# @Software:PyCharm

"""
构造表达式
列表生成式，一次性全部生成，比较占用内存
"""

myList = [x * x for x in range(10)]  # x,生成一个列表0~9，返回数据为x*x
print(myList, type(myList))

myList2 = [x * x for x in range(1, 10) if x > 5]  # 生成一个列表1~9,判断限制的是range(1,10)生成的列表返回为大于5的x给到x*x
print(myList2, type(myList2))
