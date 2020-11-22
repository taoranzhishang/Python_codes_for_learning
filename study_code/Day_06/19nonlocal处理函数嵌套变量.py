def fun1():
    num = 1
    print(num,id(num))
#由于python可以函数嵌套定义，所以有引用外层
    def fun2():
        # num=0#内层变量覆盖外层，两个不是同一个变量
        nonlocal num  # 引用外层变量，用于函数嵌套；global引用全局变量
        num = 0
        print(num, id(num))

    fun2()
    print(num, id(num))


# print(mum)#局部变量外部不能使用


fun1()
