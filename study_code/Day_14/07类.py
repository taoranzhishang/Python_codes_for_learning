"""
类可以实现数据和代码的重用
"""


class name_age:  # class 类的标识，用于定义类，nameMoney类的名称，类的内部是属性和方法,使用.可以调用属性和方法
    def __init__(self, name, age, money):  # self 自身，实例化后就是其自身
        # print("hello world")
        self.name = name  # 属性
        self.age = age  # 属性
        self.money = money  # 属性

    def saveMoney(self, num):  # 方法，行为
        print(self.name, "存款", num)
        self.money += num

    def withdrawMoney(self, num):  # 方法，行为，可以实现某种功能
        print(self.name, "取款", num)
        self.money -= num


print(type(name_age))  # <class 'type'>，类类型
cl1 = name_age("coder", 20, 100000)  # 类的实例化，创建一个对象，调用init函数
print(type(cl1))  # <class '__main__.nameAge'>
# print(nameAge())  # <__main__.nameAge object at 0x000001F2784DA0A0>
print(cl1.name, cl1.age)  # 调用属性
cl1.saveMoney(100)  # 调用方法
cl1.withdrawMoney(100)

cl2 = name_age("colder", 20, 1000000)
print(cl2.name, cl2.age)
cl2.saveMoney(1000)
cl2.withdrawMoney(10000)
