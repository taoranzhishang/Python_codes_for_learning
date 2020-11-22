set1={1,2,3,4,5}
set2={1,2,7,8,9}
set3={5,2,3,4,1}
set4={1,2,3,4,5,7,8}
set5={1,2,3,4,5,6}

print(set1-set2)#set1有set2没有
print(set2-set1)#set2有set1没有

print(set1&set2)#交集
print(set2|set1)#并集
print(set1^set2)#并集-交集：两个集合独有的

print(set1==set3)#True，判断两个集合元素是否相等，无序

print(set4.difference(set5))#找出set4集合对于sset4集合中有差异的部分，{8, 7}
print(set5.difference(set4))#找出set5集合对于sset4集合中有差异的部分，{6}

print(1 in set1)#True 用于判断元素是否在结构中
print(10 in set1)#False，元素不在结构中
print(10 not in set1)#True，元素在结构中