num = 1
print(type(num))
num = str(num)  # int型转换为str
print(type(num))
num1 = 1.0
print(type(num1))
num1 = int(num1)  # 实型转换为int型
print(type(num1))
str = "1.0"  # 字符串本身是字符int不能转换
# str1="1"
str1 = "num"
print(type(str))
print(type(str1))
# str=int(str)
str = eval(str)  # str转换为数值型，整数字符串转换为整数，实数转换为实数
str1 = eval(str1)  # 数据本身不是数值的还是原类型
print(type(str))
print(type(str1))

num2=1
#print(type(str(num2)))
print(type(num2))