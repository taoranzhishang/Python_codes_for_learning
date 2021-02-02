def makename(name):
    if name.find("SB") != -1:
        print(name)
        raise NameError  # 主动提示异常

    print("OK")
    return name


print(makename("SB1"))

'''
try:
    print(makename("SB1"))
except:  # 遇到错误，被动异常
    print("error")
'''
