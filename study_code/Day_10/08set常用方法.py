myset={1,2,3,4,5}
print(myset)
# myset.remove(7)  #删除，没有元素报错
myset.discard(7)#删除，没有元素不报错
print(myset)

myset.pop()
print(myset)#弹出1  print(myset.pop())

newset=myset.copy()#深复制
print(newset)
print(myset.clear())#清空，