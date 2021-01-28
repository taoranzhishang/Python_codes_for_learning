import itertools

"""
m选n个-->m!/n!(m-n)!
"""
numList = list(itertools.combinations([1, 2, 3, 4], 3))  # 4个元素取3个为一组，无序，元素相同算一个
print(len(numList))
print(numList)
