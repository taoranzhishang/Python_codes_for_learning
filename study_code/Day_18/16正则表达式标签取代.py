import re

"""
\\1 代表前面重复部分
所替换的部分必须括起来整体替换，对应匹配
"""
str1 = "<title>helloworld</title>"
# str1 = "<title>helloworld</titles>"

re1 = re.match("<[A-Za-z]*>\w*</[A-z]*>", str1)
print(re1)  # <re.Match object; span=(0, 25), match='<title>helloworld</title>'>
re2 = re.match("<([A-z]*)>\w*</\\1>", str1)
print(re2)  # <re.Match object; span=(0, 25), match='<title>helloworld</title>'>
