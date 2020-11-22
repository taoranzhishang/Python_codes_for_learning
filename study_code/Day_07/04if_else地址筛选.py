import os


def fun(str):
    if str.find("12345") != -1:  # 找到返回位置，找不到返回-1
        os.system("echo password is right")
    else:
        os.system("echo password is not right")


str = "12457895"
print = fun
print(str)
