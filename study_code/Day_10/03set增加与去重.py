myset = {1, 2, 3, 4, 5, 6}
print(myset)
myset.add(7)  # 末尾插入7
myset.add(1)  # 重复，无作用，去重
print(myset)

strset = set("abcdefg")  # 乱序
print(strset)
strset.update("12345abcd")  # 将字符串打碎插入到strset里，去除重复归并
print(strset)

# myset.update(8)  #单个字符不可以插入，tuple、list、字符串可以
myset.update([8])  # 插入list
myset.update((9,))  # 插入tuple
print(myset)
