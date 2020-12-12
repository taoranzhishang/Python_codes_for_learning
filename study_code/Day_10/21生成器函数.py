# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    21生成器函数.py
# @Time:    2020/12/12 18:12
# @Software:PyCharm


"""
def creatList():
    myList=[x for x in range(1000)]#一次性全部生成，费内存
    return myList
print(creatList())#不带yield可以直接调用
"""


def creatList2():
    for i in range(1000):
        print(i)
        yield i


x = creatList2()  # 将生成器函数返回值赋值给x，不是调用，不会输出
print(type(creatList2))  # <class 'function'>
print(type(creatList2()))  # <class 'generator'>
print(type(x))  # <class 'generator'>
"""
将生成器函数赋值给x，相当于每次都要进入x，即进入函数，但是数据会更新，不同于直接调用生成器函数
每次都是第一次进入，所以返回值不变
"""
next(x)  # next，从第一个开始，带yield只能用next调用--> next(creatList()) 进入函数才会打印
next(x)
next(x)
