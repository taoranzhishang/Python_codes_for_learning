import numpy as np

arr1 = np.arange(1, 7).reshape(3, 2)  # 生成一个1~8得数组，再转换为4行2列得二维数组
arr2 = np.arange(7, 1, -1).reshape(3, 2)
# print(arr)  # 输出数组
# print(arr[2])  # 输出下标为2的元素
# print(arr[1:3])  # 输出下标1~2的元素
print(arr1)
print(arr2)
print(np.add(arr1, arr2))  # 求对应元素的和
print(np.subtract(arr1, arr2))  # 求对应元素的差
print(np.multiply(arr1, arr2))  # 乘积
print(np.divide(arr1, arr2))  # 除
print(np.floor_divide(arr1, arr2))  # 整除
print(np.negative(arr1))  # 元素相反数
print(np.mod(arr1, arr2))  # 求模
print(np.power(arr1, arr2))  # 指数
