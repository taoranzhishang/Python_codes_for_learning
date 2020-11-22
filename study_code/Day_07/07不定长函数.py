def add(*num):  # *num表示一个序列，有多个数据
    result = 0
    for data in num:  # data轮询传入的每一个num
        result += data
    print(result)


add(1)
add(1, 2)
add(1, 2, 3)
