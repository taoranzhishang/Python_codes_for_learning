mylist = [1, 2, 3, 4, 5, 6]
print(len(mylist))
for data in mylist:  # 遍历列表并打印
    print(data)
mylist.append('a')  # 末尾加上字符,数字均可
for data in mylist:
    print(data)

print(mylist)  # 全部
print(mylist[:])  # 全部
print(mylist[:6])  # 0到5位
print(mylist[4:])  # 4到末尾
print(mylist * 2)
print(mylist + mylist[3:7])  # 截取，相加
ls = []
ls1 = [1]
print(type(ls), type(ls1))
