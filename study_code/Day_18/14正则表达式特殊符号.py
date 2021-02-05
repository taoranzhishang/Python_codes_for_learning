import re

s1 = re.search(r"(?:abc){2}", "abcabc")  # ?:有与没有没区别，没有实际意义
print(s1)  # <re.Match object; span=(0, 6), match='abcabc'>

"""
DeprecationWarning: Flags not at the start of the expression '((?i)abc){2}'
  s2=re.search(r"((?i)abc){2}","abcABC")
"""
s2 = re.search(r"((?i)abc){2}", "abcABC")  # 忽略大小写
print(s2)  # <re.Match object; span=(0, 6), match='abcABC'>

s3 = re.search(r"(abc(?#注释)){1}", "abc")  # ?#正则表达式的注释
print(s3)  # <re.Match object; span=(0, 3), match='abc'>

s4 = re.search(r"(a(?=1bc))", "a1bc")  # 以1bc结尾，才能匹配a
print(s4)  # <re.Match object; span=(0, 1), match='a'>

s5 = re.search(r"(a(?=1bc))", "abc")  # 未以1bc结尾
print(s5)  # None

s6 = re.search(r"(a(?!bc))", "acb")  # 不能以bc结尾，才能匹配a
print(s6)  # <re.Match object; span=(0, 1), match='a'>

s7 = re.search(r"(a(?!bc))", "abc")
print(s7)  # None

s8 = re.search(r"((?<=bc)a)", "bca")  # 以bc开头才能匹配a
print(s8)  # <re.Match object; span=(2, 3), match='a'>

s9 = re.search(r"(?<=bc)a", "cba")  # 未以bc开头
print(s9)  # None

s10 = re.search(r"(?<!bc)a", "cba")  # 不以bc开头才能匹配a
print(s10)  # <re.Match object; span=(2, 3), match='a'>

s11 = re.search(r"(?<!bc)a", "bca")  # 以bc开头
print(s11)  # None
