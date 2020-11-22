mylist=[1,2,3,4,5,6]
print(mylist)


for i in range(len(mylist)):#修改列表必须用索引
    if mylist[i]==2:
        mylist[i]=-2
        print(mylist[i])
print(mylist)
'''
for data in mylist:#data相当于副本，改变副本不影响list元素值，修改失败，用于读取不修改
    if data==2:
        data=-2
        print(data)#data可以改变，但元素不变
print(mylist)
'''