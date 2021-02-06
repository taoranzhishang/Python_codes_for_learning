import re

str1 = "<title>百度一下，你就知道</title>"
str2 = "<HTML><title>百度一下，你就知道</title></HTML>"

re1 = re.match("<[\w]*>.*<[/\w]*>", str1)
print(re1)  # <re.Match object; span=(0, 24), match='<title>百度一下，你就知道</title>'>
re2 = re.match("<[\w]*><[\w]*>.*</[\w]*></[\w]*>", str2)
print(re2)  # <re.Match object; span=(0, 37), match='<HTML><title>百度一下，你就知道</title></HTML>'>

"""
引用分组数字匹配到的字符串
(\w*) \\1
(\w*) (\w*)  \\2 \\1
"""
re3 = re.match("<(\w*)>.*</\\1>", str1)
print(re3)  # <re.Match object; span=(0, 24), match='<title>百度一下，你就知道</title>'>
re4 = re.match("<(\w*)><(\w*)>.*</\\2></\\1>", str2)
print(re4)  # <re.Match object; span=(0, 37), match='<HTML><title>百度一下，你就知道</title></HTML>'>
