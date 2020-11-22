import random


def show1():  # 定义一个函数，没有参数，没有返回值
    print("python")


show1()  # 函数调用


def show2(num):  # 有参数，无返回值
    print("python", num)


for i in range(5):
    show2(i)


def show3():  # 无参数，有返回值
    return random.randint(0, 100)


num = show3()
print(num)


def add(num1, num2):  # 有参数，有返回值
    return num1 + num2


print(add(3, 4))
