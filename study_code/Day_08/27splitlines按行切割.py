str = """
锄禾日当午，
活在天朝真是苦
aaaaa
bbbbb
"""

print(str.splitlines())  # 按行切割，默认换行，返回list
print(str.splitlines(True))  # 参数为True，换行两次，返回list
str1 = str.splitlines()
str2 = str.splitlines(True)
for i in str1:
    print(i)
for j in str2:
    print(j)
