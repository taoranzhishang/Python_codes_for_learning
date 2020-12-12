"""
迭代器主要用于循环
列表转换为迭代器，使用next进行迭代
"""

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
it = iter(mylist)  # it迭代器，记录list的索引，next一次，索引后移一个
print(it)  # <list_iterator object at 0x0000026B0D3B0820>
print(type(it))#<class 'list_iterator'>迭代器类型
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(mylist)  # 自动记录索引，tuple，list，set，dict通用
for i in it:
    print(i)
