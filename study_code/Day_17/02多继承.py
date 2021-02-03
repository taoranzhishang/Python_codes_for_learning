class 美女演员的亲爹:
    def __init__(self):
        self.money = 10000
        self.bike = "自行车"
        self.livein = "天桥下"

    def buy(self):
        print("买不起车，买不起房，消费不起高级化妆品")

    def do(self):
        print("农民工")


class 美女演员的干爹:
    def __init__(self):
        self.money = 200000000
        self.car = "兰博基尼"
        self.house = "上海滩1号"

    def bigbuy(self):
        print("没有什么爷我买不起的")

    def do(self):
        print("土豪")


class 美女演员(美女演员的干爹, 美女演员的亲爹):  # 继承两个类
    def __init__(self):
        """
        初始化，后者覆盖前者
        """
        美女演员的亲爹.__init__(self)
        美女演员的干爹.__init__(self)

    def wanto(self):
        print("可以被潜规则，但是一定有钱花")


# 多继承，同时继承两个类的属性，方法，


jt = 美女演员()
"""
因为：属性对于每个对象私有，方法共享的
"""
'''
属性与初始化顺序，后者覆盖前者
美女演员的干爹.__init__(self)
美女演员的亲爹.__init__(self)
'''
print(jt.money)  # 10000 属性后者覆盖前者
print(jt.car)
print(jt.bike)
print(jt.livein)
print(jt.house)

'''
方法与继承顺序有关，前者覆盖后者
美女演员的干爹,美女演员的亲爹
'''
jt.wanto()
jt.buy()
jt.bigbuy()
jt.do()
