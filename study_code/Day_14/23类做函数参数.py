class Cl:
    num = 0

    def show(self):
        print(self.num)


def change1(data):  # data接收实参，为类类型
    """
    函数内重新实例化同名对象并修改，不改变函数外同名对象的值
    """
    d1 = Cl()  # 重新实例化一个对象d1与外部的d1无关，函数内的局部变量，只在函数内生效，外部不可调用
    d1.show()  # 0 类变量初始值
    d1.num = 100  # 动态绑定修改
    d1.show()  # 200


def change2(data):  # data接收实参，为类类型
    """
    实例对象作为参数传入并修改会改变函数外对象的值
    """
    data.num = -1  # 修改的是类的属性，会改变原值
    data.show()


d1 = Cl()
d1.show()
d1.num = 1  # 动态绑定修改属性
d1.show()  # 1
change1(d1)  # 类作为参数
d1.show()  # 重新实例化进行的修改不影响外部的值1，改变函数内变量地址，函数外的不能改变
change2(d1)
d1.show()  # 作为参数传入函数并动态修改后是-1，直接从类内部操作，结果会改变，改变了地址
