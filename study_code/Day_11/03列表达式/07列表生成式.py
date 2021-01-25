# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    07列表生成式.py
# @Time:    2020/12/13 0:07
# @Software:PyCharm
myList1 = [x for x in range(1, 101, 2)]  # 一般形式
print(myList1)

myList2 = [x + 1 for x in range(1, 101, 2) if x < 50]  # 一般形式+判断
print(myList2)

myList3 = [[x, x + 1, x * x] for x in range(1, 101, 2) if x > 50]  # 生成一个列表嵌套一个列表，二维列表，判断限制的是range()生成的列表
print(myList3)

myList4 = [x + y for x in range(10) for y in range(10)]  # 嵌套循环，总共100次，内层循环一次外层再循环
print(myList4)

myList5 = [[x, y] for x in range(10) for y in range(10)]  # x=0,y从0~9，x=1，y从0~9……x=9，y从0~9
print(myList5)

myList6 = [str([x, y]) for x in range(10) for y in range(10)]  # 返回后再转换为str
print(myList6)
