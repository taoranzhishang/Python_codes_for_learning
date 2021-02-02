num1 = eval(input("num1:"))
num2 = eval(input("num2:"))
try:  # 尝试
    print(num1 / num2)  # ZeroDivisionError: division by zero
except ZeroDivisionError:  # 处理错误
    print("num2不可以为0")
print("一定要记住哦")
