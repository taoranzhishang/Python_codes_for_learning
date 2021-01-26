mydict = {"abcd": 10, "123": 10}
mydict2 = {"love": 100}
print(len(mydict))  # 求长度，键值对的个数，2
print(str(mydict))  # 转换为str类型，{'abcd': 10, '123': 10}，字典每个符号都转为字符：括号、引号、字符……
for i in str(mydict):
    print(i)

newdict = mydict  # 浅复制
print(newdict)
mydict["abcd"] = 0
print(newdict)

newmydict = mydict.copy()  # 深复制
mydict["abcd"] = 100
print(newmydict, mydict)

# mydict.clear()#清空

print(mydict.get("abcd"))  # 获取对应下标的value
print(mydict.get("bacde"))  # 没有则返回None
print(mydict["abcd"])  # 获取对应下标的value，
# print(mydict["abcde"])#没有则报错

print(mydict.items())  # 以元组形式返回dict_items([('abcd', 100), ('123', 10)])
print(mydict.keys())  # 获取所有的key，dict_keys(['abcd', '123'])
print(mydict.values())  # 获取键值，dict_values([100, 10])

mydict.update(mydict2)  # 字典拼接，多合一
print(mydict)

mydict.setdefault("abc", 10)  # 不存在添加指定键值对
mydict.setdefault("abcd", None)  # 存在无操作
print(mydict)

for key in mydict.keys():  # 遍历每一个key
    print(key)

for data in mydict.values():  # 遍历value
    print(data)
