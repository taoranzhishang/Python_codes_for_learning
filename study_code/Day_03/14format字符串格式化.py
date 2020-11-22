# format()格式化，默认右对齐，加<左对齐
# 10表示宽度，.5表示小数点后5位，转换码f表示浮点数

print(type(format(1, "2d")))  # format()的返回值是str
# 原数据宽度大于转换宽度按原宽度,小数点等符号也占一个宽度
print(format(12345, "1d"))
print(format(100.1, "10.5f"))
print(format(100.12, "10.5f"))
print(format(100.123, "10.5f"))
print(format(100.1234, "10.5f"))
print(format(100.12345, "10.5f"))

print(format(100.1, "<10.5f"))
print(format(100.12, "<10.5f"))
print(format(100.123, "<10.5f"))
print(format(100.1234, "<10.5f"))
print(format(100.12345, "<10.5f"))

# 右对齐，宽度10，转换码d表示整型
print(format(1001, "10d"))
print(format(10012, "10d"))
print(format(100123, "10d"))
print(format(1001234, "10d"))
print(format(10012345, "10d"))
# <表示左对齐
print(format(1001, "<10d"))
print(format(10012, "<10d"))
print(format(100123, "<10d"))
print(format(1001234, "<10d"))
print(format(10012345, "<10d"))
# 转换码s表示字符串
print(format("1001", "10s"))
print(format("10012", "10s"))
print(format("100123", "10s"))
print(format("1001234", "10s"))
print(format("10012345", "10s"))
