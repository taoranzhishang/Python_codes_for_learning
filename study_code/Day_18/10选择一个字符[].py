import re

"""
[abcd] abcd中间取一个，匹配的字符第一个在就匹配
[^abcd] 非abcd，第一个匹配则匹配
"""
regex1 = re.compile("[abcd]", re.IGNORECASE)
print(regex1.match('a'))  # <re.Match object; span=(0, 1), match='a'>
print(regex1.match('b'))  # <re.Match object; span=(0, 1), match='b'>
print(regex1.match("ab"))  # <re.Match object; span=(0, 1), match='a'>

regex2 = re.compile("[^abcd]", re.IGNORECASE)
print(regex2.match('a'))  # None
print(regex2.match('e'))  # <re.Match object; span=(0, 1), match='e'>
print(regex2.match("ae"))  # None
print(regex2.match('ea'))  # <re.Match object; span=(0, 1), match='e'>

"""
[0-9]数字
[^0-9]非数字
"""
regex3 = re.compile("[0-9]", re.IGNORECASE)
print(regex3.match('9'))  # <re.Match object; span=(0, 1), match='9'>
print(regex3.match('a'))  # None

regex4 = re.compile("[^0-9]", re.IGNORECASE)
print(regex4.match('9'))  # None
print(regex4.match('a'))  # <re.Match object; span=(0, 1), match='a'>

"""
[a-z]小写字母
[^a-z]非小写字母
"""
regex5 = re.compile("[a-z]", re.IGNORECASE)
print(regex5.match('v'))  # <re.Match object; span=(0, 1), match='v'>
print(regex5.match('7'))  # None

regex6 = re.compile("[^a-z]", re.IGNORECASE)  # re.IGNORECASE 忽略大小写
print(regex6.match('v'))  # None
print(regex6.match('7'))  # <re.Match object; span=(0, 1), match='7'>
print(regex6.match('A'))  # None，re.IGNORECASE 忽略大小写
print(regex6.match('7'))  # <re.Match object; span=(0, 1), match='7'>

"""
[0-8A-z]数字0-8，大小写字母
[0-9A-Za-z]
"""
regex7 = re.compile("[0-8A-z]", re.IGNORECASE)
print(regex7.match('7'))  # <re.Match object; span=(0, 1), match='7'>
print(regex7.match('9'))  # None
print(regex7.match('a'))  # <re.Match object; span=(0, 1), match='a'>

"""
[0-9][a-z] 第一个字符0-9，第二个小写字母，匹配两个
[][]1对中括号代表一个字符
"""
regex8 = re.compile("[0-9][a-z]", re.IGNORECASE)
print(regex8.match('9'))  # None
print(regex8.match('a'))  # None
print(regex8.match("9P"))  # <re.Match object; span=(0, 2), match='9P'>，re.IGNORECASE 忽略大小写
