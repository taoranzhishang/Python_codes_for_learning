import os  # 系统自带函数，builtin_function_or_method

print(type(print), id(print))  # 系统自带函数
print(type(os.system), id(os.system))


def fun():
    print("fun")


print(type(fun), id(fun))  # 自定义函数，function
