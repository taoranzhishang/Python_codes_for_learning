"""
私有属性作用域为类内
"""
class Money1:
    def __init__(self):
        self.money = 100

    def show(self):
        print(self.money)


class Money2:
    def __init__(self):
        self.__money = 100

    def show(self):
        print(self.__money)


myMoney1 = Money1()
myMoney1.money = -100  # 动态绑定修改，只能影响实例属性、方法
myMoney1.show()  # -100
myMoney2 = Money2()
myMoney2.__money = -100  # 修改只在外部有效，不影响类内的私有属性，相当于新的变量，不在类内
# print(myMoney2.__money)  # -100 私有属性只在类内生效，外部可调用，不可更改，若没有上一行就会报错，因为未定义该变量
myMoney2.show()
