mylist = [1, 2, 3, 4, 5]
newlist = mylist  # 浅复制，实际上是复制同一个地址，一个改变，另一个跟着改变
print(mylist, id(mylist))
print(newlist, id(newlist))

mylist[0] = -1
print(mylist, id(mylist))
print(newlist, id(newlist))

lastlist = mylist.copy()  # 深复制，赋值了一个新的地址，二者不是同一个变量地址，
# 一个改变，另一个不会改变
# 或使用遍历逐个取值赋值
print(mylist, id(mylist))
print(lastlist, id(lastlist))
mylist[0] = 1
print(mylist, id(mylist))
print(lastlist, id(lastlist))
