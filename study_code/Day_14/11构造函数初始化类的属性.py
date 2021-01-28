class MyClass:
    # 类中函数外不能使用self.
    # a = 1  # 属性在构造函数外一般可省略，在构造函数内进行初始化
    # b = 1

    def __init__(self, x, y):
        """
        类中默认有构造函数，但是可以重写，解决变量初始化
        """
        print("created")
        # print(self.a, self.b)
        self.a = x
        self.b = y

    def add(self):
        return self.a + self.b

    def __del__(self):
        print("deleted")


cl1 = MyClass(100, 200)  # 构造函数，传递参数初始化
print(cl1.add())
