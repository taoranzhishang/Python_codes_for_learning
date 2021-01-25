myset = {1, 2, 3, 4, 5}
print(myset)
# myset.remove(7)  #删除，没有元素报错
myset.discard(7)  # 删除，没有元素不报错，若存在删除所有指定值
print(myset)
"""
集合在定义后第一次输出时会自动升序排列，排序后pop()时是可以确定的
在为排序前集合顺序随机，弹出的左边第一个值不确定
"""
# myset={'1','a',1,'b',2}
# print(myset)
temp = myset.pop()
print(temp,myset)  # 弹出左边第一个，在为排序前集合顺序随机，弹出的左边第一个值不确定
print(myset.pop())
newset = myset.copy()  # 深复制
print(newset)
print(myset.clear())  # 清空
