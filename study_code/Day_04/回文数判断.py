num = eval(input("请输入一个三位数："))

if (num // 100 > 0 and num // 100 < 10):  # 判断是否是三位数
    if num // 100 == num % 10:
        print("是回文数")
    else:
        print("不是回文数")
else:
    print("不是三位数")
