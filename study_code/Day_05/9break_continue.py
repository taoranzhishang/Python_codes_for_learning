num = eval(input("please input a num:"))
for i in range(10):
    if i == num:
        print("find")
        # break#结束循环
        continue  # 结束本次循环，开始下一次循环
    print(i)
