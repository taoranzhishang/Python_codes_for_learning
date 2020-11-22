def add(num1, num2):
    return num1 + num2


num = add(1, 2)  # num为返回值类型
print(num, type(num))
print(id(add))  # 函数的地址，操作地址可以做很多事情
print(type(add))  # 函数的类型，function类型

'''
函数本质是一个地址，修改地址可以实现不同的行为
'''


def fun1():
    print("fun1")


def fun2():
    print("fun2")


go = fun1

go()
print(id(go), id(fun1))
print(type(go), type(fun1))

go = fun2

go()
print(id(go), id(fun2))
print(type(go), type(fun2))
