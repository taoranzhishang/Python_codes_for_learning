num = 1  # 全局变量，全局使用
num1 = 2


def fun():
    num = 100  # 局部变量，只能在局部代码块内部使用
    num2 = 100  # 局部变量，外部不能使用
    global num1  # 加上以后，引用全局
    num1 = 0  # 将0的地址赋值给num1
    print(num1, id(num1))
    print(num, id(num))


print(num1, id(num1))
fun()
print(num, id(num))
# print(num2)#外部使用函数内部的局部变量会标红
print(num1, id(num1))  # 全局引用后被修改
