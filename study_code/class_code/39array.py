import numpy as np

arr1 = np.array([[0], [1], [2], [3]])  # .reshape(2, 2)  # 四行1列数组
arr2 = np.array([1, 2, 3])  # 一维数组
print(arr1)
print(arr2)
print(np.add(arr1, arr2))  # 触发广播机制
'''
广播机制的触发
若4*3
有：
一维数组
4*3
4行1列数组
'''