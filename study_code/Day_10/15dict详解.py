mydict = {"abcd": 10, "123": 10}
mydict2 = {"love": 100}
print(len(mydict))  # 求长度，2
print(str(mydict))  # 转换为str类型，{'abcd': 10, '123': 10}

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

mydict.update(mydict2)  # 字典拼接
print(mydict)

mydict.setdefault("abc", 10)  # 不存在添加默认值
mydict.setdefault("abcd", None)  # 存在无操作
print(mydict)

for key in mydict.keys():  # 遍历每一个key
    print(key)

for data in mydict.values():  # 遍历value
    print(data)
