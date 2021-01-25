tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple2 = (6, 7, 8, 9, 10)

print(tuple1[:])  # 全部
print(tuple1[2:])  # 2到最后
print(tuple1[:-2])  # 0到-3
print(tuple1[2:-2])  # 2到-3

print(tuple1 + tuple2)  # 拼接
print(tuple2 * 4)  # 复制4次

# del tupel1[1]  #不能清除元素
del tuple2  # 清除内存，无法再次调用
# print(tuple2)

print(len(tuple1))  # 长度
print(5 in tuple1)  # 存在
print(100 not in tuple1)  # 不存在

for data in tuple1:  # data是副本，但tuple元素不支持修改
    print(data)

print(max(tuple1))
print(min(tuple1))
newtuple = tuple([1, 23, 3, 3])  # 类型转换，使list不能被修改
print(newtuple)
