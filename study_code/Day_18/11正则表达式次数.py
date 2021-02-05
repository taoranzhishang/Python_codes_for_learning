import re

"""
* 0次或无限次
使用*所有都匹配，因为0次匹配也算匹配
"""
regex1 = re.compile("\\d*", re.IGNORECASE)
print(regex1.match("7"))  # <re.Match object; span=(0, 1), match='7'>
print(regex1.match("76"))  # <re.Match object; span=(0, 2), match='76'>
print(regex1.match("76a"))  # <re.Match object; span=(0, 2), match='76'>  *匹配次数不限，两次匹配就算匹配
print(regex1.match("a76"))  # <re.Match object; span=(0, 0), match=''> 0次匹配也算匹配

"""
+ 1次或无限次，第一个不匹配就算不匹配，第一个以后的不匹配算匹配
"""
regex2 = re.compile("\\d+", re.IGNORECASE)
print(regex2.match("7"))  # <re.Match object; span=(0, 1), match='7'>
print(regex2.match("76"))  # <re.Match object; span=(0, 2), match='76'>
print(regex2.match("76a"))  # <re.Match object; span=(0, 2), match='76'>
print(regex2.match("a76"))  # None

"""
? 0次或1次
0次匹配算匹配，1次匹配算匹配，超过1次只匹配1次
"""
regex3 = re.compile("\\d?", re.IGNORECASE)
print(regex3.match("7"))  # <re.Match object; span=(0, 1), match='7'>
print(regex3.match("76"))  # <re.Match object; span=(0, 1), match='7'>
print(regex3.match("76a"))  # <re.Match object; span=(0, 1), match='7'>
print(regex3.match("a76"))  # <re.Match object; span=(0, 0), match=''>
print(regex3.match("abcd"))  # <re.Match object; span=(0, 0), match=''>

"""
{n} n次
低于n次的匹配算匹配返回None，超过n次只匹配n次
"""
regex4 = re.compile("\\d{2}", re.IGNORECASE)
print(regex4.match('5'))  # None
print(regex4.match("56"))  # <re.Match object; span=(0, 2), match='56'>
print(regex4.match("567"))  # <re.Match object; span=(0, 2), match='56'>

"""
{1,3} 1-3次，{4，10}4-10次
{m,n} m-n次
从左第一个开始，低于m次匹配算匹配实际次数返回None，高于n次匹配只算n次，从左开始次数限制内有不匹配的不算
"""
regex5 = re.compile("\\d{1,3}", re.IGNORECASE)
print(regex5.match('5'))  # <re.Match object; span=(0, 1), match='5'>
print(regex5.match("56"))  # <re.Match object; span=(0, 2), match='56'>
print(regex5.match("567"))  # <re.Match object; span=(0, 3), match='567'>
print(regex5.match("5678"))  # <re.Match object; span=(0, 3), match='567'>
print(regex5.match("a567"))  # None
print(regex5.match("ab56"))  # None
print(regex5.match("abc5"))  # None
print(regex5.match("abcd"))  # None
