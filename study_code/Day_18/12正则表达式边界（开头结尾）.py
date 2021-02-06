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
\b…… 必须转义
\b 是正则表达式规定的一个特殊代码（好吧，某些人叫它元字符，metacharacter），代表着单词的开头或结尾，也就是单词的分界处。
虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是\b并不匹配这些单词分隔字符中的任何一个，它只匹配一个位置。
\b 匹配这样的位置：它的前一个字符和后一个字符不全是(一个是,一个不是或不存在) \w。
"""
# s5=re.search(r"\bthe"," the those three")  # the
# s5=re.search(r"\bthe","athe those three")  # not found
# s5 = re.search("\\bthe", "athea those three")# not found
s5 = re.search("\\bthe", "thea those three")
if s5 is not None:
    print(s5.group())  # the
else:
    print("not found")

"""
\B…… 可以不转义
\B 匹配这样的位置：它的前一个字符和后一个字符全是(一个是,一个不是或不存在) \w。
"""
# s5 = re.search("\Bthe", "athea those three")  # the
s5 = re.search("\Bthe", "the those three")
if s5 is not None:
    print(s5.group())  # not found
else:
    print("not found")
