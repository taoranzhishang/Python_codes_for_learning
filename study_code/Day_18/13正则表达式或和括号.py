import re

"""
str1|str2 与两个字符（串）中的一个匹配即可
"""
s1 = re.search("abc|xyz", "abc")
if s1 is not None:
    print(s1.group())  # abc
else:
    print("not found")
"""
abc{n}：c匹配n次，低于n次不算，高于n次算n次
abc{m,n}：c匹配m-n次，低于m次不算，高于n次算n次
(abc){n}：括号内整体匹配n次，低于m次不算，高于n次算n次
(abc){m,n}：括号内整体匹配m-n次，低于m次不算，高于n次算n次
"""
s2 = re.search("abc{2,4}", "abccccc")  # 最后一个字符c匹配2-4次,低于2次不算匹配，高于4次算4次
if s2 is not None:
    print(s2.group())  # abcccc
else:
    print("not found")

s3 = re.search("(abc){2,4}", "abcabc")  # 括号内匹配2-4次，低于2次不算，高于4次算4次
if s3 is not None:
    print(s3.group())  # abcabc
else:
    print("not found")

# s3 = re.search("abc(abc){2,4}", "abcabcabc")  # abcabcabc
s3 = re.search("abc(abc){2,4}", "abcabcabc")  # 括号内匹配2-4次，低于2次不算，高于4次算4次
if s3 is not None:
    print(s3.group())
else:
    print("not found")  # not found

s4 = re.search(r"(abc){2}", "abcabc")  # abc匹配2次
print(s4)  # <re.Match object; span=(0, 6), match='abcabc'>

s5 = re.search(r"(abc|xyz){2}", "abcxyz")  # abc或xyz任意匹配2次，这里各匹配
print(s5)  # <re.Match object; span=(0, 6), match='abcxyz'>

s6 = re.search(r"(abc|xyz){2}", "abcabc")  # abc或xyz任意匹配2次，这里abc匹配2次
print(s6)  # <re.Match object; span=(0, 6), match='abcabc'>

s7 = re.search(r"(abc|xyz){2}", "abcxya")  # abc或xyz任意匹配2次，abc只匹配一次，xya不匹配
print(s7)  # None
