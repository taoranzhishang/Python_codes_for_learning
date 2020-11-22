# round(x,y)四舍五入x，精确到小数点后y位

money = input("please input your money")
print(money)
money = eval(money)  # 字符串转整数
print(int(money), '元', int(money * 10) % 10, '角', round(money * 100 % 10), '分')
