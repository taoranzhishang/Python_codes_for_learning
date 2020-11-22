mystr = "hello world,hello world"

print(mystr.capitalize())  # 首字母大写

str = "8888"
for i in range(6, 40, 2):
    for j in range((40 - i) // 2, 0, -1):
        print(' ', end='')
    print(str.center(i, '*'))  # 返回一个指定宽度居中的字符串，默认填充空格，i为宽度，
                                # ""填充字符fillcharcenter(i,"8")

print(mystr.count("h"))  # 判断字符字符串出现的次数
print(mystr.count("he", 10))  # 判断字符字符串出现的次数,从位置10开始
print(mystr.count("he", 10, 15))  # 位置10到15
