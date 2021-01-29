class cl:

    def display1(self):
        print("有名对象")

    def display2(self):
        print("匿名对象")


cl1 = cl()  # 实例化有名对象
cl1.display1()  # 调用有名对象的方法
cl().display2()  # 调用匿名对象方法，与匿名函数一样，没有名字只能用一次
