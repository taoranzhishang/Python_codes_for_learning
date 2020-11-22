mylist1=[1,2,3,4,5,6]
mylist2=[6,6,6,1,22,33,44,55,66,12]
print(1 in mylist1)#判读存在
print(1 not in mylist2)#判断不存在
print(mylist1+mylist2)#拼接，两个和为一个；归并是去除重复的
print(mylist1*4)#连续复制4遍，四个为一个list
print(len(mylist1),len(mylist2))#求长度
print(max(mylist1))
print(min(mylist2))
for data in mylist1:#遍历list，只读不改
    print(data,end=" ")
