"""
super解决父类重复初始化，节约内存
"""


# class 爷:
#     def __init__(self):
#         print("爷构造了一次")
#
#
# class 大儿子(爷):
#     def __init__(self):
#         爷.__init__(self)
#         print("大儿子构造了1次")
#
#
# class 二儿子(爷):
#     def __init__(self):
#         爷.__init__(self)
#         print("二儿子构造了1次")
#
#
# class 小儿子(爷):
#     def __init__(self):
#         爷.__init__(self)
#         print("小儿子构造了1次")
#
#
# class 媳妇(大儿子, 二儿子, 小儿子):
#     def __init__(self):
#         """
#         从上往下初始化
#         """
#         大儿子.__init__(self)
#         二儿子.__init__(self)
#         小儿子.__init__(self)
#
#
# xf = 媳妇()

class 爷:
    def __init__(self):
        print("爷构造了一次")


class 大儿子(爷):
    def __init__(self):
        super().__init__()
        print("大儿子构造了1次")


class 二儿子(爷):
    def __init__(self):
        super().__init__()
        print("二儿子构造了1次")


class 小儿子(爷):
    def __init__(self):
        super().__init__()
        print("小儿子构造了1次")


class 媳妇(小儿子, 二儿子, 大儿子):  # 继承顺序从右往左
    def __init__(self):
        super().__init__()


xf = 媳妇()
