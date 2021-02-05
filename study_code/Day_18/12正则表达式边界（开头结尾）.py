import re

# m = re.search("^the", "these the good man")
m = re.match("the", "the good man")  # 匹配字符串以……开头
if m is not None:
    print(m.group())  # the
else:
    print("not found")

s = re.search("the", "those the good man")  # 搜索含有……
if s is not None:
    print(s.group())  # the
else:
    print("not found")

"""
^…… 匹配字符串的开头，多行模式的每一行开头
"""
# s1 = re.search("^the", "athe good man")  # not found
# s1 = re.search("^the", "these the good man")  # the
s1 = re.search("^the", "those the good man")  # 搜索以……开头，等价match
if s1 is not None:
    print(s1.group())
else:
    print("not found")  # not found

s2 = re.search("^the", "the good man")
if s2 is not None:
    print(s2.group())  # the
else:
    print("not found")

"""
\A…… 匹配字符串以……开头，可以不转义
"""
# s3 = re.search("\Athe", "athe good man")  # not found
# s3 = re.search("\Athe", "these good man")  # the
# s3 = re.search("\Athe", "those good man")  # not found
# s3 = re.search("\\Athe", "the good man")
# s3 = re.search(r"\Athe", "the good man")
s3 = re.search("\Athe", "the good man")
if s3 is not None:
    print(s3.group())  # the
else:
    print("not found")

"""
……$ 匹配字符串以……结尾，多行模式的每一行开头
"""
# s4 = re.search("the$", "three the those")  # not found
# s4 = re.search("the$", "three the\r\n those")  # not found 换行符无效
# s4 = re.search("the$", "three those aaathe")  # the
# s4 = re.search("the$", "three those the ")  # not found 空格结尾不匹配
s4 = re.search("the$", "three those the")
if s4 is not None:
    print(s4.group())  # the
else:
    print("not found")

"""
……\Z 匹配字符串以……结尾，可以不转义
"""
# s4 = re.search("the$", "three the those")  # not found
# s4 = re.search("the$", "three the\r\n those")  # not found 换行符无效
# s4 = re.search("the$", "three those aaathe")  # the
# s4 = re.search("the$", "three those the ")  # not found 空格结尾不匹配
# s4 = re.search("the\\Z", "three those the")
# s4 = re.search(r"the\Z", "three those the")
s4 = re.search("the\Z", "three those the")
if s4 is not None:
    print(s4.group())  # the
else:
    print("not found")

"""
\b…… 字符串内部，先匹配单词字符在匹配非单词字符，必须转义
--> ……是\w与\W任意两个中间的部分
"""
# s5=re.search(r"\bthe"," the those three")  # the
# s5=re.search(r"\bthe"," athe those three")  # the
s5 = re.search("\\bthe", "the those three")  # 与上面不同，\b须转义
if s5 is not None:
    print(s5.group())  # the
else:
    print("not found")

"""
\B…… 全部不匹配，可以不转义
待验证：……的两边不能是单词字符和非单词字符
"""
s5 = re.search("\Bthe", "the those three")  # 与上面不同，\b须转义
if s5 is not None:
    print(s5.group())  # not found
else:
    print("not found")
