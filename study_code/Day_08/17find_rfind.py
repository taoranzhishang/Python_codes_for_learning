str = "中国 美国 英国 台湾 中国"
print(str.find("美国"))  # 字符串中查找内容，找到返回首个匹配的字符下标，未找到返回-1
print(str.find("中国", 0, 2))  # 第一个参数为指定查找的内容，第二个参数为开始查找的位置，
                                # 第三个参数为结束查找的位置
print(str.find("中国", 1, 1))  # 异常，未将字符串全部包括
print(str.find("中国", 3, 0))  # 异常
print(str.find("中国"))  # 从头部开始，返回第一个下标
print(str.rfind("中国"))  # 从头部开始，返回最后一个字符的下标
print(str.rfind("中国", 6))
print(str.rfind("中国", 6, len(str)))
