# 类-->人类-->动物类-->生物
# 对象-->个人就是实例化的对象
# 任何一个数据都是一个对象
print(type("abc"))  # abc就是一个str类型的对像，对象就可以调用方法
print("abc".upper())  # upper()将小写转换为大写
print("HELLO".find("w"))  # 字符串中找到E的位置，找到返回位置，未找到返回-1
print("HELLO".lower())  # 转换为小写

str = "abcd"
str1 = str.upper()
print(str1)
