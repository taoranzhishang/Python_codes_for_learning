myset={12,34,5,6,6}
print(myset)

'''
set不能使用下标，所以不能直接修改单个元素，只能转换为list
'''

newset=list(myset)
for i in range(len(newset)):
    newset[i]=0

print(newset)