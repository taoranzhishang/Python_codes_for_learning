class C:
    def __init__(self):
        self.name = "Colder"

    @classmethod  # 标识符，可省略，表示类的内部方法
    def func1(self):
        print("func1")

    def func2(self):
        print("func2")


def func(obj):  # 类的实例化对象作为参数，外部方法
    obj.func1()
    obj.func2()
    return obj.name


person = C()
print(func(person))  # 将实例化对象作为函数参数，函数内调用对象属性，方法
