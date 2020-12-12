# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    02myQueue.py
# @Time:    2020/12/12 23:09
# @Software:PyCharm


"""
最小生成树：将很多点用最短的路径连接起来
最短路径：一个点到另一个点的最短路径
"""

import collections  # 数据结构集合

queue = collections.deque([1, 2, 3, 4, 5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())  # 获取所弹出queue左边的第一个，打印
print(queue)
