class sizeException(Exception):  # 继承关系
    def __init__(self, errorvalue):  # 错误代码初始化
        self.value = errorvalue

    def __str__(self):  # str() #转化为字符串
        return self.value


class Box:
    def __init__(self, x, y, z):
        if x > 10:
            raise sizeException("big")  # 触发一个匿名对象表示错误
        elif x < 2:
            raise sizeException("small")
        if y > 10 or y < 2:
            raise 2  # 报错，提示2，无法处理2
        if z > 10 or z < 2:
            raise 3
        # self.x = x
        # self.y = y
        # self.z = z


try:
    b1 = Box(1, 4, 5)
except sizeException as  e:  # as把一个类型当作一个对象，e对象名称
    print("异常", e.value)
