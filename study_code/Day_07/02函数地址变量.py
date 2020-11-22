def add(num1, num2):
    return num1 + num2


def mul(num1, num2):
    return num1 * num2


fun = add
print(fun(1, 2))
fun = mul
print(fun(1, 2))

add = mul  # 不符合软件工程规范不可以使用，规范常量
print(add(1, 2))
