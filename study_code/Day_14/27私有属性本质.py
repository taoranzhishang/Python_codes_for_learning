class Cl:
    def __init__(self):
        self.__num = 100  # 私有属性

    def show(self):
        print(self.__num)  # 私有方法

    def __show(self):
        print("外部访问私有方法")


d1 = Cl()
# d1.show()
d1._Cl__num = 0  # 外部访问私有属性，对象名._类名__私有属性名
d1.show()
d1._Cl__show()  # 外部访问私有方法，对象名._类名__私有方法名
print(dir(Cl))
