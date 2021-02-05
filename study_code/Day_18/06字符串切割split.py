import re

# str1="1234566 abcdef"
# print(str1.split(" "))


str2 = "127740 1小姐    22   166 本科  未婚   合肥 山羊座  编辑 普通话"
str2Split = re.split("\\s+", str2)
print(str2Split)

str3 = "a b,c;d"
str3Split = re.split(r"[\s\,\;]", str3)  # 3个中任意一种都切掉
print(str3Split)
