# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    06排序密码文件.py
# @Time:    2021/1/9 12:21
# @Software:PyCharm

filepath = r"D:\code\py\study_code\Day_12\userPassword.txt"
file = open(filepath, "rb")
dataline = file.readlines()
dataline.sort()
file.close()

userPassword_filepath1 = r"D:\code\py\study_code\Day_12\userPassword1.txt"
userPassword1 = open(userPassword_filepath1, "wb")
for password in dataline:
    userPassword1.write(password)
userPassword1.close()
