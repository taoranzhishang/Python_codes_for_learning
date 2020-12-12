# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    01myStack.py
# @Time:    2020/12/12 22:58
# @Software:PyCharm

"""
stack
先进后出，后进先出
"""

myStack = []
print(myStack)
myStack.append(1)
print(myStack)
myStack.append(2)
print(myStack)
myStack.append(3)
print(myStack)
myStack.append(4)
print(myStack)

myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)

"""
进一个，出一个,先进先出
"""
myStack2 = []
print(myStack2)
myStack2.append(1)
print(myStack2)
myStack2.pop()
print(myStack2)
myStack2.append(2)
print(myStack2)
myStack2.pop()
print(myStack2)
myStack2.append(3)
print(myStack2)
myStack2.pop()
print(myStack2)
