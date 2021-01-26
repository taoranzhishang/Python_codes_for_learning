myset = {1, 2, 3, 4, 5, 6}
print(myset)
myset.add(7)  # 末尾插入7
myset.add(1)  # 重复，无作用，去重
myset.add('a')  # 字符不自动排序
myset.add(0)  # 数值自动排序
print(myset)  # {0, 1, 2, 3, 4, 5, 6, 7, 'a'}

strset = set("abcdefg")  # 乱序，每个字符为一个元素
print(strset)
strset.update("12345abcd")  # 将字符串打碎插入到strset里，去除重复归并
print(strset)

# myset.update(8)  # 单个数值不可以插入，tuple、list、字符串可以
myset.update([8])  # 插入list
myset.update((9,))  # 插入tuple
myset.update('8')  # 单个字符可以插入
print(myset)
