myset = {1, 2, 3, 4, 5}
for data in myset:  # 副本，修改不影响原本
    print(data)

# print(myset[0])  #set无序，没有索引

for idx, iddata in enumerate(myset):  # enumerate枚举生成索引，副本
    print(idx, iddata)  # idx为下标，iddata为元素
