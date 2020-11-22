mytuple = (1, 2, 3, 4, 5)
mylist = [1, 2, 3, 4, 5]
mydict = {1, 2, 3, 4, 5}
print(1 in mylist)  # 用于判断存在或不存在元组，列表，字典中
print(10 not in mylist)

for i in mytuple:  # i在mytuple中遍历，不能使用not in
    pass
