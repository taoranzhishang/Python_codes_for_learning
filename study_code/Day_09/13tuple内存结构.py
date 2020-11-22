mytuple=(1,2,3,4,5)#每个元素是地址常量，不可以修改
print(mytuple)
for i in range(len(mytuple)):
    print(mytuple[i],id(mytuple[i]))
#mytuple[1]=100
mytuple=0,0,0,0,0
print(mytuple)#内部元素是常量不可以修改，但可以为tuple赋值一个新的元组地址