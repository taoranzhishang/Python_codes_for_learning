str = "中国 美国 英国 台湾 中国"
print(str.index("中国"))  # 查找字符串是否存在，存在返回第一个下标，不存在引发异常错误
print(str.index("中国", 3, len(str)))
print(str.rindex("中国"))  # 查找字符串是否存在，存在返回最后一个下标，不存在引发异常
print(str.rindex("日本", 0, len(str)))#未找到，引发异常
