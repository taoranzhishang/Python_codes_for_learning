import re
"""
re.subn的返回值为tuple，替换后结果和次数统计
re.sub的返回值为str，只有替换后结果，没有次数统计
"""
str1 = "包子 包子 包子 包子 包子"
str2 = re.subn("包子", "馒头", str1)  # 所有的包子替换为馒头，次数5
print(type(str2))  # <class 'tuple'> 返回值类型tuple
print(str2)  # ('馒头 馒头 馒头 馒头 馒头', 5)
print(str2[0])  # 馒头 馒头 馒头 馒头 馒头
print(str2[1])  # 5

str3 = "包子 包子 包子 包子 包子"
str4 = re.subn("包子", '', str1)  # 删除，所有的包子替换为空，次数5
print(str4)  # ('    ', 5)
print(str4[0])  #
print(str4[1])  # 5

str5 = "123 321 4562415 812479 212 33 "
str6 = re.subn("\\d+", "abc", str5)
print(str6)  # ('abc abc abc abc abc abc ', 6)

str7 = "123 321 4562415 812479 212 33 "
str8 = re.sub("\\d+", "abc", str7)
print(type(str8))#<class 'str'> 返回一个str
print(str8)  # abc abc abc abc abc abc