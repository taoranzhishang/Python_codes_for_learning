import re

"""
先进行预编译，处理大数据
"""

Str1 = "12345566700----colder1030"
pat = re.compile("(.*)----(.*)")  # 对表达式进行预编译
matchObj = pat.match(Str1)
print(matchObj)
print(matchObj.group())#与0等价
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))
