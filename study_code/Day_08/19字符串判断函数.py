print("hello123啊".isalnum())  # 判断字符串是字母或数字，汉字作字母，返回true或false
print("hello啊".isalpha())  # 判断字符串是纯字母
print("123".isdigit())  # 判断字符串是纯数字
print("ABC啊".isupper())  # 判断全是大写，汉字不分大小写
print("abc啊".islower())  # 判断全是小写，汉字不分大小写
print("Hello World".istitle())  # 元素首字母大写，其他字母小写返回true
print("123".isdecimal())  # 判断10进制数
print("0xa1".isdecimal())  # 不能说明其它进制
print("0xa1".isdigit())  # 返回false，不能说明其它进制
print("12".isnumeric())  # 判断纯数字
print(" ".isspace())  # 判断是否为空字符
