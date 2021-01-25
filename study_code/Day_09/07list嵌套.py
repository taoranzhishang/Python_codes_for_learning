list1 = [1, 2, 3]
list2 = [4, 5, 6, ["abcd"]]
list3 = [7, 8, 9]
mylist = [list1, list2, list3]  # 每个元素为一个list
print(mylist)
for List in mylist:  # 遍历mylist中的元素，每个元素是list
    print(List)

for List in mylist:  # 遍历mylist中的元素，每个元素是list
    for data in List:  # 在第一次遍历的list元素中遍历元素
        print(data)
