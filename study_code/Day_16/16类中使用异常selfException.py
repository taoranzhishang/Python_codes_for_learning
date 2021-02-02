class Box:
    def __init__(self, x, y, z):
        if x > 10 or x < 2:
            raise 1
        if y > 10 or y < 2:
            raise 2  # 报错，提示2，无法处理2
        if z > 10 or z < 2:
            raise 3
        self.x = x
        self.y = y
        self.z = z


try:
    b1 = Box(13, 4, 5)
except 1:  # 无法处理1，except只接受异常类型
    print("1 error")
except:
    print("无异常")


