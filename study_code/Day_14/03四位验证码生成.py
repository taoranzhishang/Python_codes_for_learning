import itertools

pwdList = ["".join(x) for x in
           itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=4)]  # 生成一个4位元素列表
# print(pwdList)
print(len(pwdList))
file = open("4pwd.txt", "wb")
for pwd in pwdList:
    file.write((pwd + "\r\n").encode("utf-8"))
file.close()
