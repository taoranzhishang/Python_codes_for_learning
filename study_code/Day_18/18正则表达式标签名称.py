import re

str1 = "<HTML><title>百度一下，你就知道</title></HTML>"
re1 = re.match("<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", str1)
print(re1)  # <re.Match object; span=(0, 37), match='<HTML><title>百度一下，你就知道</title></HTML>'>
