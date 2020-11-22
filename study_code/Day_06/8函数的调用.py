def fun1():
    print("fun1")


def fun2():
    print("fun2")


def fun3():
    print("fun3")


# 函数调用必须等到返回后才能执行下一步
# 函数的调用自上而下，按照先后顺序1,2,3执行,瀑布执行
fun1()
fun2()
fun3()


# 函数的嵌套调用
def fun1():
    fun2()
    print("fun1")


def fun2():
    fun3()
    print("fun2")


def fun3():
    print("fun3")


fun1()
