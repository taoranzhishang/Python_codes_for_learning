fz = frozenset([1, 2, 3, 4, 5])  # 不可变集合

print(fz, type(fz))
for data in fz:
    print(data)
# print(fz[0]),不能取下标，不能修改，不能增加删除
# set可以增删，不能改变单个元素，不能取下标
for id, iddata in enumerate(fz):
    print(id, iddata)  # id为下标，iddata为元素
