# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    08矩阵生成.py
# @Time:    2020/12/13 0:28
# @Software:PyCharm
#
myList = []
for i in range(10):  # i控制行数
    """
    生成一个10嵌套10个元素的列表
    """
    myList.append([i * 10 + j for j in range(10)])  # j控制列数
print(myList)

for i in myList:  # 输出一个元素为一个10个元素的列表
    print(i)

myList2 = []
for l in range(0, 8, 7):  # 控制步长实现取值需求
    myList2.append([l + j for j in range(1, 8)])

for l in myList2:
    print(l)
"""
[1, 2, 3, 4, 5, 6, 7]
[8, 9, 10, 11, 12, 13, 14]
"""
