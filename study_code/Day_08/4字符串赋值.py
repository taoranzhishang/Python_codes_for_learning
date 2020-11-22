str = "hello world"
print(str)
# str[5]='a'#字符串赋值实质是赋值的地址，字符串不能修改单个字符，只能整体重新赋值一个地址
str = "abcd"
print(str)
str = str[3]
print(str)
print("\a")  # 失效
