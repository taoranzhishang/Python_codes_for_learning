# 整数，字符串有副本机制

def changing(num):
    print(num, id(num))  # 原本
    num = 100  # 副本
    print(num, id(num))


def changing1(str):
    print(str, id(str))  # 原本
    str = "hello"  # 副本
    print(str, id(str))


num = 10
print(num, id(num))
changing(num)  # 传入参数会重新开辟内存，新建变量
print(num, id(num))  # 原来的变量不被改变

str = "你好"
print(str, id(str))
changing1(str)
print(str, id(str))  # 原本
