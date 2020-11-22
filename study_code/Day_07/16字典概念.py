mydict = {"abc": 1, "def": 2, "ghi": 3}  # dict是set的加强，
                                    # 左边是key不允许重复，右边是value可以重复
print(type(mydict))  # dict类型
print(mydict)

print(mydict["abc"])  # 根据key取出value，字典索引
print(mydict.values())  # 打印所有值

for key in mydict:  # 循环字典
    print(key, mydict[key])

mylist = [1, 2, 3, 4]
myset = frozenset(mylist)

mylist[2] = 100
# myset[2]=100#set不支持索引，tuple和list支持数字索引，dict支持key索引

print(mylist)
print(myset)
