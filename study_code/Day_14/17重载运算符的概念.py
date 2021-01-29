"""
complex复数
1+2i + 3+4i = 4+6i
"""


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
        print(self.x, other.x)
        print(self.y, other.y)
        self.x += other.x
        self.y += other.y


cl1 = complex(1, 2)
cl2 = complex(3, 4)
cl1.show()
cl2.show()
# cl1 + cl2  # 与下一行等价，结果赋值给了前面的cl1，使用cl1.show()调用
cl1.__add__(cl2)#谁调用结果给谁，用谁调用其它方法
# cl2 + cl1  # 谁在前结果给谁，使用cl2.show()调用
cl1.show()
# cl2.show()  # 对cl2对象原样输出，加法改变了cl1未改变cl2
"""
对于其它的类型以上方法不起作用
"""
print(1+2)
print('1'+'2')