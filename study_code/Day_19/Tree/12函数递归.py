def func3():
    print("Func3 Start")
    func2()
    print("Func3 End")


def func2():
    print("Func2 Start")
    print("Func2 End")


def func1():
    print("Func1 Start")
    func3()
    print("Func1 End")


func1()
