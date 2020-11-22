# 交互对称赋值，两边必须个数相同
num1, num2, num3 = 1, 2, 3
print(num1, num2, num3)
num1, num2, num3 = num3, num2, num1  # 交互赋值实现数据交换
print(num1, num2, num3)
