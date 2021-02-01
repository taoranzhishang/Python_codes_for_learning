class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, '+', self.y, 'i')

    # def __add__(self, other):
    #     print(other.x, other.y)
    #     return complex(self.x + other.x, self.y + other.y)  # 加法的返回值
    #
    # def __add__(self, num):
    #     print(self.x, num)
    #     print(self.y, num)
    #     return complex(self.x + num, self.y + num)  # 加法的返回值
    def __add__(self, other):
        if type(self) == type(other):  # 判断类型，重载complex+complex
            print(other.x, other.y)
            return complex(self.x + other.x, self.y + other.y)
        if type(other) == type(10):  # 判断类型，重载complex+int
            return complex(self.x + other, self.y + other)


cl1 = complex(1, 2)
cl2 = complex(3, 4)
cl1.show()
cl2.show()
# cl3=cl1.__add__(10)
# cl3=cl1.__add__(cl2)
# cl3 = cl1 + cl2  # 不能分辨使用哪个add，不能解释
# cl3.show()
# cl4 = cl1 + 10  # 只用了第二个add,但是可以运行,可以重新解释
# cl4.show()

cl5 = cl1 + cl2
cl6 = cl1 + 10
cl5.show()
cl6.show()
