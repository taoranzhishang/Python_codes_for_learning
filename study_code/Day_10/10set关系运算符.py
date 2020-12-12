set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 5, 1}
set3 = {2, 3, 4, 5, 6}
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set1 == set2)  # True,元素相同，无序
print(set1 != set3)  # True,元素不同,无序

print(set1 <= set2)  # True,set1包含于set2
print(set1 < set2)  # False，set1真含于set2
print(set1 <= set4)  # True，set1包含于set4

print(set2 <= set1)  # set2包含set1
print(set2 < set1)  # set2真包含set1

print(set1.issuperset(set2))  # True,set1是否包含set2
print(set1.issubset(set2))  # True,set1是否被set2包含
