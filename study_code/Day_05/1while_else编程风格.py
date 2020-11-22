password = input("please input your password:")
pas = "123456"
while password != pas:
    password = input("your password is not right,please input again:")
else:  # 不满足循环条件时，恰好跳出循环
    print("password is right")
