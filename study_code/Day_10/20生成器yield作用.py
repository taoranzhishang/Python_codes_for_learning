# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    20生成器yield作用.py
# @Time:    2020/12/12 17:54
# @Software:PyCharm

"""
函数执行，一次性完成
"""
def fun1():
    print(1)
    print(2)
    print(3)

fun1()
print(type(fun1))#<class 'function'>
print(type(fun1()))#<class 'NoneType'>,先调用函数打印1，2，3，然后无返回值，默认None
"""
函数内生成器
yield 分段返回,只起到返回作用，不会打印
"""
def fun2():
    print(1)
    yield -1
    print(2)
    yield -2
    print(3)
    yield -3

fun2()
print(type(fun2))#<class 'function'>
print(type(fun2()))#<class 'generator'>，先调用函数打印1，2，3，加上yield的返回值是生成器

num=fun2()#调用函数，赋值给num，分段返回，一个yield返回一次，生成器只能用next调用
print(type(num))#<class 'generator'>
print(next(num))#打印返回值-1
print(next(num))#打印返回值-2
print(next(num))#打印返回值-3
#print(next(num))#超过范围，报错