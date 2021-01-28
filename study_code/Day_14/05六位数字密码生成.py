import itertools

pwdList = ["".join(x) for x in itertools.product("0123456789", repeat=6)]  # 6位元素列表
print(len(pwdList))
file = open("6pwd.txt", "wb")
for pwd in pwdList:
    file.write(((pwd + "\r\n").encode("utf-8")))
file.close()
