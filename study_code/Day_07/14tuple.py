mytuple = (1, 23, 4, 5, 6)

print(mytuple)
print(len(mytuple))

for i in mytuple:  # 遍历内容
    print(i)  # 打印内容

for i in range(len(mytuple)):  # i在长度中遍历
    print(mytuple[i])  # i作为索引

# mytuple[1]=100  # tuple不可以修改内部数据,list可以。但是可以重新赋值一个地址
mytuple = (12, 3, 4, 5, 6, 5, 7)
print(mytuple)
print(len(mytuple))
print(mytuple[:])

tuple1 = ()  # tuple类型
tuple2 = (1,)  # tuple类型
tuple3 = (1)  # int类型
tuple4 = 1,  # tuple类型
print(type(tuple1), type(tuple2), type(tuple3), type(tuple4))
