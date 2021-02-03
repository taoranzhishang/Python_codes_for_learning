class 王健林:
    def __init__(self):
        self.name = "王健林"
        self.mystr = "先定一个小目标，赚它一个一亿"
        self.money = 200000000000


class 王思聪(王健林):  # 继承，父类
    def __init__(self):
        super().__init__()  # 调用王健林打下的根基     super()父类，初始化，
        self.mystr = "论投胎的重要性"
        self.name = "王思聪"


china王健林 = 王健林()
china王思聪 = 王思聪()
print(china王健林.name)
print(china王健林.money)
print(china王健林.mystr)

print(china王思聪.name)
print(china王思聪.money)
print(china王思聪.mystr)
