import os

str = os.popen("ping www.baidu.com")
str = str.read()
print(str)
if str.find("请求超时") != -1:
    print("连接失败")
else:
    print("连接成功")
