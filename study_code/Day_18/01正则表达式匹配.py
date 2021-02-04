import re

"""
[1-9] 第一个字符1-9；\\d 转义字符\d，数字；{4，10} 4-10位
print(re.match("[1-9]\\d,{4,10}","1213a4"))
"""

"""
匹配，从左边第一个起
匹配不成功返回None，匹配成功返回位置详细信息
"""
print(re.match("abc", "abc"))  # <re.Match object; span=(0, 3), match='abc'>
print(re.match("xabc", "abc"))  # None
print(re.match("abc", "xabc"))  # None
print(re.match("abcx", "abc"))  # None
print(re.match("abc", "abcx"))  # <re.Match object; span=(0, 3), match='abc'>

"""
match严格匹配，abc在abcdef左边第一个开始逐个匹配
"""
matchObj = re.match("abc", "abcdef")
print(type(matchObj))  # <class 're.Match'>
print(matchObj)  # <re.Match object; span=(0, 3), match='abc'>
print(matchObj.group(0))  # abc 挖掘第一个字符串

"""
r表转义
.表示任意字符不包括换行，*表示0次或n次
有几个正则表达式，group()的次数不能超过
"""
Str = "colder is handsome isn't ugly"
matchStr = re.match(r"(.*) is (.*)", Str)
print(matchStr)  # <re.Match object; span=(0, 29), match="colder is handsome isn't ugly">  详细匹配信息，从0-28位
print(matchStr.group(0))  # colder is handsome isn't ugly  整体
print(matchStr.group(1))  # colder  第1个正则表达式
print(matchStr.group(2))  # handsome isn't ugly  第2个正则表达式

"""
切割
"""
Str1 = "12345566700----colder1030"
matchStr1 = re.match(r"(.*)----(.*)", Str1)
print(matchStr1)  # <re.Match object; span=(0, 25), match='12345566700----colder1030'>
print(matchStr1.group(0))  # 12345566700----colder1030
print(matchStr1.group(1))  # 12345566700
print(matchStr1.group(2))  # colder1030
