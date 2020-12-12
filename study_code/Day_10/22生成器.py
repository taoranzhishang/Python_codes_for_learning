# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    22生成器.py
# @Time:    2020/12/12 20:42
# @Software:PyCharm


def fun():
    for i in range(1,101):
        yield i

print(fun())#直接调用不能：<generator object fun at 0x000002697FF7BCF0>
print(type(fun))#<class 'function'>
print(type(fun()))#<class 'generator'>
print(next(fun()))#1每次都调用函数，从第一步开始，值不会变化
print(next(fun()))#1
"""
将生成器函数赋值给x，相当于每次都要进入x，即进入函数，但是数据会更新，
不同于直接调用生成器函数，每次调用都是新一次的进入，所以返回值从头开始
"""
x=fun()#好比调用后赋值给x，再操作x，一次进行，
print(next(x))
print(next(x))
print(next(x))
