mylist = [1, 2, "12", True, 4, 5]  # lsit中每一个元素都有一个地址，元素是变量可以修改，地址是常量
print(id(mylist))
for data in mylist:
    print(data, id(data))
'''
for i in range(len(mylist)):
    print(mylist[i],id(mylist[i]))
'''
