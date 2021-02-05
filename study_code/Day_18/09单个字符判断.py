import re

"""
. 表示除换行\n以外的所有字符
\ 转义字符：\t \r \n \b
\d 数字
\D 非数字
\s 空白字符，空格，\t
\S 非空白字符
\w 单词字符，字母大小写、数字、下划线
\W 非单词字符
"""
regex1 = re.compile(".", re.IGNORECASE)
print(regex1.match("a"))  # <re.Match object; span=(0, 1), match='a'>

regex2 = re.compile(".")
print(regex2.match("\n"))  # None

regex3 = re.compile(".")
print(regex3.match("\t"))  # <re.Match object; span=(0, 1), match='\t'>

regex4 = re.compile("\\t")
print(regex4.match("\t"))  # <re.Match object; span=(0, 1), match='\t'>

regex5 = re.compile(r"\d")
print(regex5.match('5'))  # <re.Match object; span=(0, 1), match='5'>
print(regex5.match('A'))  # None

regex6 = re.compile(r"\D")
print(regex6.match('A'))  # <re.Match object; span=(0, 1), match='A'>
print(regex6.match("5"))  # None

regex7 = re.compile(r"\w")
print(regex7.match('a'))
print(regex7.match('A'))
print(regex7.match('5'))
print(regex7.match(';'))  # None

regex8 = re.compile(r"\W")
print(regex8.match('a'))
print(regex8.match('A'))
print(regex8.match('5'))
print(regex8.match(';'))  # <re.Match object; span=(0, 1), match=';'>
