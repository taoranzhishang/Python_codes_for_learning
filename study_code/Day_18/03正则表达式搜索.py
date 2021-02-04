import re

"""
匹配，第2个表达式从第1个字符开始要与第一个字符匹配，匹配返回第1个表达式在第2个表达式的位置信息，不匹配返回None
搜索，只要第2个表达式包含第1个表达式即可，搜索到返回第1个表达式在第2个表达式的位置信息，未搜索到返回None
"""

print(re.match("abc","abc xyz"))#<re.Match object; span=(0, 3), match='abc'>
print(re.match("abc","xyz abc"))#None

print(re.search("abc","abc xyz"))#<re.Match object; span=(0, 3), match='abc'>
print(re.search("abc","xyz abc"))#<re.Match object; span=(4, 7), match='abc'>

searchObj=re.search("abc", "abc xyz")
print(searchObj.group())#abc
print(searchObj.group(0))#abc

"""
空格算作字符，表达式没有指明不会切割
"""
searchObj1=re.search(r"(.*)-#-(.*)#-(.*)","abc cba -#- xyz #-zyx")
print(searchObj1)#<re.Match object; span=(0, 21), match='abc cba -#- xyz #-zyx'>
print(searchObj1.group())#abc cba -#- xyz #-zyx
print(searchObj1.group(0))#abc cba -#- xyz #-zyx
print(searchObj1.group(1))#abc cba
print(searchObj1.group(2))# xyz
print(searchObj1.group(3))#zyx
