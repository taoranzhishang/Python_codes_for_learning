import itertools

"""
<itertools.permutations object at 0x0000020B1A342040>
"""
numList = list(itertools.permutations([1, 2, 3, 4], 3))  # 排列4个数的列表，3个数为一组，有序，全排列
print(len(numList))
print(numList)
"""
阶乘
n!=n*(n-1)*(n-2)*...*2*1
排列：m选n个-->m!/(m-n)!
"""
