"""
面向过程实现
"""
# def HaveMeal(name):
#     print(name, "走路")
#     print(name, "排队")
#     print(name, "选餐")
#     print(name, "付费")
#     print(name, "吃饭")
#
#
# name = "coder"
# HaveMeal(name)
"""
面向对象实现
"""


class HaveMeal:
    def __init__(self, name):
        self.name = name
        age = 20
        weight = 100

    def HaveMeal(self):
        print(self.name, "走路")
        print(self.name, "排队")
        print(self.name, "选餐")
        print(self.name, "付费")
        print(self.name, "吃饭")


name = "colder"
eating = HaveMeal(name)
eating.HaveMeal()
