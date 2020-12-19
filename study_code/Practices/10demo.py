# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    10demo.py
# @Time:    2020/12/14 17:08
# @Software:PyCharm

"""
第一个调用先进行：1: []
               2: [1]
第二次调用后进行：1: [1]    元素是第一次调用时加入的
               2: [1, 1]
两次调用返回的结果：[1, 1] [1, 1]
"""


def func(x=[]):
    # print("1:", x)
    x.append(1)
    # print("2:", x)
    return x


print(func(), func())
