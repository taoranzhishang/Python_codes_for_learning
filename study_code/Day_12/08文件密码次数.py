# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    08文件密码次数.py
# @Time:    2021/1/9 13:07
# @Software:PyCharm
filepath = r"D:\code\py\study_code\Day_12\csdnpassword.txt"
file = open(filepath, "rb")
dataline = file.readlines()
dataline.sort()
file.close()

userPassword_filepath1 = r"D:\code\py\study_code\Day_12\csdnpassword1.txt"
userPassword1 = open(userPassword_filepath1, "wb")
for password in dataline:
    userPassword1.write(password)
userPassword1.close()

filepath = r"D:\code\py\study_code\Day_12\csdnpassword1.txt"
file = open(filepath, "rb")
pwdList = file.readlines()
length = len(pwdList)
file.close()

passwordpath = r"D:\code\py\study_code\Day_12\csdnpasswordtimes.txt"
csdnpassword = open(passwordpath, "wb")

i = 0
while i < length:
    counter = 1
    password = pwdList[i].decode("utf-8")
    while i + 1 <= length - 1 and pwdList[i].decode("utf-8") == pwdList[i + 1].decode("utf-8"):
        counter += 1
        i += 1
    else:
        i += 1
        csdnpassword.write((str(counter) + ' ' + password).encode("utf-8"))
csdnpassword.close()
print("finish")
