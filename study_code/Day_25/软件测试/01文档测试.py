"""
一般程序员，测试函数，测试函数可靠性，文档测试
有一个错误都会报错
"""


def add(x, y):
    """
    这是一个函数
     :param x:参数1
     :param y:参数2
     :return x+y:返回x+y
>>> print(add(1,2))  # 与>>>平齐
3
 >>> print(add(1,-1))
 0
     """
    return x + y


import doctest

doctest.testmod()
print(add(1, -1))
