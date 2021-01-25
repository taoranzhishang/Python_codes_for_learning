mylist = [1, 2, 3, 4, 5, 1, 6, -1, 1, -2, 1.1]
print(mylist)

mylist.append(7)  # 尾部添加7，会改变原list的值
mylist.append('a')  # 尾部添加字符a，会改变原list的值
print(mylist)

print(mylist.count(7))  # 7的个数，出现次数
print(mylist.index('a'))  # 查找第一个出现的下标，未找到则引发异常

mylist.remove(1)  # 从左起删除第一个值为1的元素，没有则报错
print(mylist)

del mylist[len(mylist) - 1]  # 删除list最后一个元素，会改变原list的值
print(mylist)
mylist.sort()  # 升序排序，会改变原list的值,数值型与字符型不能直接比较，所以删除字符a
print(mylist)

mylist.reverse()  # 反转，会改变原list的值
print(mylist)
'''一个小插曲
del mylist[9]
print(mylist)
mylist.sort()
print(mylist)
'''
temp = mylist.pop()  # 弹出最后一个元素，返回末尾元素并删除末尾元素
print(temp)
print(mylist)

mylist.insert(2, "ntm")  # 在下标为2处插入数据，原元素后移
print(mylist)
mylist.clear()  # 清除所有元素，倒水留杯子
print(mylist)
