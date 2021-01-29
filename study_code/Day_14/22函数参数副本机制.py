def change(tnum):
    print("change", id(tnum), tnum)  # change 3043698570336 (1,)；接收时仍为实参
    tnum = -1,  # 有操作后新建副本
    print("change", id(tnum), tnum)  # change 3043727790768 (-1,)


def change1(temp):
    print("change1", id(temp), temp)  # change1 3043780936512 [1, 2, 3, 4]
    temp[0] = -1
    print("change1", id(temp), temp)  # change1 3043780936512 [-1, 2, 3, 4]


"""
字符串，整数有副本机制；元组，列表，集合，字典整体修改时有副本机制
列表，字典可以索引单个元素，因此可以改变元素，会改变原本，但不能改变整体
字符串常量不能修改内部元素，只能索引
元组不能改变单个元素，例外
集合不能索引，例外
函数调用可以改变list的元素，不能改变list的地址指向
"""
num = 1,
print("main", id(num), num)  # main 3043698570336 (1,)
change(num)
print("main", id(num), num)  # main 3043698570336 (1,)

ls = [1, 2, 3, 4]
print("main", id(ls), ls)  # main 3043780936512 [1, 2, 3, 4]
change1(ls)
print("main", id(ls), ls)  # main 3043780936512 [-1, 2, 3, 4]
