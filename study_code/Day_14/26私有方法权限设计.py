"""
私有方法只能在类内使用，外部调用报错
"""


class Bank:
    def __init__(self, pwd):
        self.__money = 0
        self.pwd = pwd

    def __check(self):
        if self.pwd == 123456:
            return True
        else:
            return False

    def saveMoney(self, money):
        self.__money += money

    def __withdrawMoney(self, money):
        if self.__check():
            self.__money -= money
        else:
            print("Password is not right.")

    def inquire(self):
        if self.__check():
            print("balance:", self.__money)
        else:
            print("Password is not right.")


print(dir(Bank))
myAccount = Bank(123456)
myAccount.saveMoney(10000)
myAccount.inquire()
