"""
enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
enumerate多用于在for循环中得到计数
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item
>>>
0 这
1 是
2 一个
3 测试

enumerate还可以接收第二个参数，用于指定索引起始值，如：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print index, item
>>>
1 这
2 是
3 一个
4 测试
"""

"""
如果要统计文件的行数，可以这样写：

count = len(open(filepath, 'r').readlines())
1
这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。

可以利用enumerate()：

count = 0
for index, line in enumerate(open(filepath,'r'))： 
    count += 1
"""
myset = {1, 2, 3, 4, 5}
for data in myset:  # 副本，修改不影响原本
    print(data)

# print(myset[0])  #set无序，没有索引

for idx, iddata in enumerate(myset):  # enumerate枚举生成索引，副本
    print(idx, iddata)  # idx为下标，iddata为元素
