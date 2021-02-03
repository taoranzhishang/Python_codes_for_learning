"""
继承的意义，代码重用，数据函数都可以重用
子类覆盖，子类与父类重名，子类覆盖父类
"""


class 王健林:
    def __init__(self):
        self.name = "王健林"
        self.money = 2000e8  # 2000*10^8
        self.myStr = "定个小目标，赚它一个亿"

    def doing(self):
        print("疯狂工作")

    def buy(self):
        print("有钱花")


class 王思聪(王健林):
    def __init__(self):
        # 王健林.__init__(self)  # 初始化父类
        super().__init__()  # 初始化父类
        self.name = "王思聪"
        self.myStr = "我交朋友不看钱，因为谁都没有我有钱"

    def doing(self):
        print("我是国民老公，想泡谁就泡谁")


dawang = 王健林()
dawang.doing()
print("王健林", dawang.money)
print(dawang.myStr)

xiaowang = 王思聪()
xiaowang.doing()
print("王思聪", xiaowang.money)
xiaowang.buy()
print(xiaowang.myStr)
