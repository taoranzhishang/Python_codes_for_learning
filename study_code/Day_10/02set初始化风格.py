set1 = set()  # 空集合
set2 = set((1, 2, 3, 4, 5, 1))  # tuple转set
set3 = set([1, 2, 3, 4, 5, 1])  # list转set
set4 = set({1: 2, 'a': 3})  # dict转set
set5 = set("abcdef")  # 字符串转set，乱序，每个字符为一个元素
set6 = {1, 2, 3, 4, 5}  # 标准风格
set0 = {}  # dict类型,空字典
print(set0, type(set0))
print(set1, type(set1))  # set() <class 'set'>  空集合
print(set2, type(set2))  # {1, 2, 3, 4, 5} <class 'set'>    去除重复
print(set3, type(set3))  # {1, 2, 3, 4, 5} <class 'set'>    去除重复
print(set4, type(set4))  # {1, 'a'} <class 'set'>   仅将key转换为set元素，键值不转换
print(set5, type(set5))  # {'b', 'c', 'd', 'a', 'f', 'e'} <class 'set'> 每个字符为一个元素
print(set6, type(set6))  # {1, 2, 3, 4, 5} <class 'set'>    标准风格

set7 = set6  # 直接复制，浅赋值
set8 = set(set7)  # 根据set初始化
print(set7, type(set8))
print(set8, type(set8))
