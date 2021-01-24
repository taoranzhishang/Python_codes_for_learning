def fun():
    return 1


def fun1():
    return 1, 2, 3


num = fun()
num1, num2, num3 = fun1()

print(num)
print(num1, num2, num3)
print(fun1(),type(fun1()))# 返回值是tuple