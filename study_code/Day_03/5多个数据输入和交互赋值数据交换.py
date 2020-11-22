num1, num2, num3 = input("请输入：")  # 依次输入三个数，用逗号隔开
print(num1, num2, num3)
# 不引入中间变量实现交换
a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = c, b, a
print(a, b, c)
