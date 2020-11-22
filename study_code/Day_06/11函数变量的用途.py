def add(num1, num2):  # 业务的逻辑
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def max(num1, num2):
    return num1 if num1 > num2 else num2


def fun(go, num1, num2):  # 接口，是不变的，业务的核心代码
    # 装饰器设计模式，函数作为参数
    return go(num1, num2)


print(fun(add, 1, 2))
print(fun(sub, 1, 2))
print(fun(max, 1, 2))
