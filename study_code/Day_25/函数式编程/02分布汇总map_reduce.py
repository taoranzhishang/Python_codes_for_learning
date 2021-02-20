def func(x):
    return x ** 2


"""
分布汇总
map分布，reduce汇总
"""

print(list(map(func, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

print(tuple(map(lambda x: -x, [1, 2, 3, 4, 5])))  # (-1, -2, -3, -4, -5)

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # 15，两辆操作


def swap(x, y):
    return x * 10 + y


print(reduce(swap, [1, 2, 3, 4, 5]))  # 12345
"""
1*10+2
12*10+3
123*10+4
1234*10+5
12345
"""
