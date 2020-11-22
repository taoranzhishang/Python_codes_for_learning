count = 1
for i in range(1000):
    if i % 10 == 0:  # 控制只打印能被10整除的数
        print(format(i, "3d"), end=" ")
        if count % 10 == 0:
            print("")
        count += 1
