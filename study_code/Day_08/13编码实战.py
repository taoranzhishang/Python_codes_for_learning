str1 = "hello world"
str2 = "你好 天朝"

print(str1.encode("utf-8"))  # b'hello world'
print(str2.encode("utf-8"))  # b'\xe4\xbd\xa0\xe5\xa5\xbd \xe5\xa4\xa9\xe6\x9c\x9d'
print((str1.encode("utf-8").decode("utf-8")))
print((str2.encode("utf-8").decode("utf-8")))  # 中文字符串，编码格式对应

print((str1.encode("utf-8").decode("gbk")))  # 英文字符串，编码格式无所谓
