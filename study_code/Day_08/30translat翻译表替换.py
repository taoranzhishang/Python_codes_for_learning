str = "hello python 我 我 我"
table = str.maketrans("op我", "000")  # 翻译替换，对应替换，可以加密，数量不对应报错
print(str.translate(table))  # str对应替换为table
print(str)#原字符串不变
