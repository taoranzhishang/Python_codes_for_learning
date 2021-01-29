class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, '+', self.y, 'i')

    def __add__(self, other):
        """
        重载：针对本类型对+重新解释一种行为
        """

        return complex(self.x + other.x, self.y + other.y)#加法的返回值


cl1 = complex(1, 2)
cl2 = complex(3, 4)
cl1.show()
cl2.show()
# cl3 = cl1 + cl2  # 与下一行等价
cl3=cl1.__add__(cl2)
cl3.show()
