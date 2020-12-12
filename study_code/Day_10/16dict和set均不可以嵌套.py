'''
set和dict都不能嵌套，不能哈希处理

'''

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5]
myset = {list1, list2}  # 不能嵌套，报错
print(myset)
