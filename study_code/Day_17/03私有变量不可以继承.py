"""
私有属性不可以继承
实例属性可以继承
"""


class dad:
    def __init__(self):
        self.money = 1e9999
        self.__wife = "***"


class kid(dad):
    def __init__(self):
        super().__init__()
        print(self.money)
        # print(self.__wife)


jc = kid()
print(jc.money)  # 实例属性可以继承
# print(jc.__wife)  # 私有属性不可以继承
