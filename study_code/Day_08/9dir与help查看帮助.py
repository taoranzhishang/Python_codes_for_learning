print(dir(""))
mylist = dir("")  # 返回值是一个列表list，包含所有的函数，和属性
for i in mylist:  # 遍历
    print(i)
    print(help("str." + i))  # help(i)查看每个函数的帮助,
    # print(help("\"\"."+i))

for i in range(len(mylist)):  # 下标法
    print(mylist[i])
    print(help("str." + mylist[i]))
'''
dir([])#[]表示一个空列表
help(list.copy)#查看copy的帮助
'''
