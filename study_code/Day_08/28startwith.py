str = "heLLo world"
print(str.startswith('he'))  # 判断以指定字符字符串开头，返回True或false
"""
对字符串中的大小写字母互换，大换小，小换大
"""
print(str.swapcase())  # 字符串小写换大写,不改变原字符串大小写
print(str)
print(str.swapcase())  # 未改变原字符串，与第一次结果相同
str1 = str.swapcase()
print(str1.swapcase())  # 字符串大写换小写
