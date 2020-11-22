list = [1, 2, 3]

list[1] = 100  # 修改
print(list)
for i in range(len(list)):  # 循环索引,取到长度，从0开始到len(list)
    print(list[i],i)
