# num = 10.4
# print(round(num))
# num2 = 10.6
# print(round(num2))  # 将浮点数转换到最近的整数，接近程度相同，转换为偶数

#银行偷窃原理
data=eval(input("输入金额："))
print((data-(data*10-int(data*10)))/10)