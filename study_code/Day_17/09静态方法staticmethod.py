class People:
    def __init__(self):
        self.height = 150
        self.money = 250

    @staticmethod  # 静态方法
    def getHeight():
        height = 100
        return height

    def getMoney(self):
        return self.money


"""
通用的方法可以写成静态方法，不实例化对象可调用，实例化后也可以调用
方便使用
"""
print(People.getHeight())
# People().getMoney()  # 匿名对象
print(type(People.getHeight), type(People.getMoney))  # <class 'function'> <class 'function'>
p1 = People()
print(p1.getHeight())
