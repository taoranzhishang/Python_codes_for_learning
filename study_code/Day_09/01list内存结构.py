mylist = [1, 2, 3, 4, 5, 6]  # list相当于一个多个变量集合，每个元素是变量地址
# 每个变量存储不同的地址，不同类型的变量地址，存储的是变量，可以修改
print(id(mylist), type(mylist), mylist)
mylist = [1, 2, 3, 4, "abc", True]#重新赋值一个list，地址改变
print(id(mylist), type(mylist), mylist)
print(id(mylist[0]), mylist[0])#内部元素的地址
print(id(mylist))
mylist[0] = -1#修改内部元素，该元素地址改变，list的地址不会改变
print(id(mylist[0]), mylist[0])
print(id(mylist))
