class cl:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)


cl1 = cl(100, 1)
cl2 = cl1  # 类的浅复制
cl3 = cl(cl1.x, cl1.y)  # 类的深复制重新实例化地址不同
cl1.show()  # 100 1
cl2.show()  # 100 1
cl3.show()  # 100 1
cl1.x = 1  # 动态绑定修改属性
cl2.y = 100
cl1.show()  # 100 1
cl2.show()  # 100 1
cl3.show()  # 1 100
print(id(cl1), id(cl2), id(cl3))  # 浅复制地址相同,深复制地址不同
"""
节约内存使用浅拷贝
保证数据安全深拷贝
"""