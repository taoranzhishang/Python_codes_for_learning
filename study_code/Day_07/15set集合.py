mylist = [1, 2, 3, 4, 5]
myset = {1, 2, 1, 1, 1, 1, 1, 2, 3, 5, 4}  # 重复只算一个,自动升序排列
set1 = {1}  # set类型
print(mylist)
print(myset)
print(type(myset))  # set类型
print(type(set1))

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 - set2)  # set1有set2没有
print(set2 - set1)  # set2有set1没有
print(set1 & set2)  # 交集
print(set1 | set2)  # 并集
print(set1 ^ set2)  # 并集-交集
