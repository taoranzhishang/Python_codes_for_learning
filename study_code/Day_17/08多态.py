"""
一个接口多个形态
使用哪个功能接口传递就可以
解决业务可拓展性，需要性能功能就新建类
"""


class Server:
    pass


class Apple(Server):
    def produce(self):
        Server.__init__(self)
        print("生产苹果")


class Orange(Server):
    def produce(self):
        Server.__init__(self)
        print("生产橘子")


def making(obj):
    obj.produce()


c1 = Apple()
making(c1)
c2 = Orange()
making(c2)
