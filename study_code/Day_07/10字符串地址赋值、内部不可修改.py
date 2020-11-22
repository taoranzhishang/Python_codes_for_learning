str = "hello world"

print(str, id(str))
str = "abcdef"
print(str, id(str))  # 地址赋值，可以将变量赋值一个新的地址

print(str[4])
# str[4]='a'#内部数据不可以改变常量字符串
print(str[4])
