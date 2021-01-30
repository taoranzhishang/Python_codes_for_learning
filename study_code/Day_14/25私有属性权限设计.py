class Bank:
    def __init__(self):
        self.__money = 0

    def saveMoney(self, money):
        self.__money += money

    def withdrawMoney(self, money):
        self.__money -= money

    def inquire(self):
        print("balance:", self.__money)


myAccount = Bank()
myAccount.saveMoney(10000)
myAccount.inquire()
myAccount.withdrawMoney(4000)
myAccount.inquire()
# myAccount.__money = 100000  # 私有属性，外部修改无效，相当于新定义
# print(myAccount.__money)  # 外部访问报错
myAccount.inquire()
