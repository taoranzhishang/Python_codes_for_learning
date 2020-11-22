'''
nuum=100
print(num)
del num
print(num)#内存回收，变量不存在
'''

mylist=[1,2,3,4,5,6]
print(mylist)
for i in range(len(mylist)):
    if mylist[i]==3:
        del mylist[i]#删除一个元素后list变小，但循环按照原来的长度执行，不跳出循环会越界
        break
print(mylist)

'''
for data in mylist:
    if data==2:
        del data#data为副本，删除不影响list元素,删除无效
        print(data)#data被删除，引用报错
'''
