mydict = {"abcd": 10, "12345": 12345}

print(mydict)

password = "abcd1"
times = 100
if password in mydict:
    mydict[password] += times  # 存在就叠加，更新 {'abcd': 110, '12345': 12345}，键值对的更新
else:
    mydict[password] = times  # 不存在就新建: {'abcd': 10, '12345': 12345, 'abcd1': 100},字典键值对的添加

print(mydict)
