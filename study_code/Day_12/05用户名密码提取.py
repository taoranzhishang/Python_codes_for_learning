# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    05用户名密码提取.py
# @Time:    2021/1/9 11:54
# @Software:PyCharm
filepath = r"D:\code\py\study_code\Day_12\demo.txt"
file = open(filepath, "rb")  # 读取结果为二进制

username_filepath = r"D:\code\py\study_code\Day_12\username.txt"
userPassword_filepath = r"D:\code\py\study_code\Day_12\userPassword.txt"
username_file = open(username_filepath, "wb")
userPassword_file = open(userPassword_filepath, "wb")

for data in file:  # 遍历数据
    # print(data)#以"wb"方式打开，结果为二进制
    data = data.decode("utf-8", "ignore")  # 对数据解码，方式为utf-8，忽略错误
    filestr = data.split(" # ")  # 切割每一行
    # print(filestr[2],end='')
    username_file.write((filestr[0] + "\r\n").encode("utf-8"))  # 将邮箱数据写入文件，编码方式utf-8
    userPassword_file.write((filestr[1] + "\r\n").encode("utf-8"))

file.close()
username_file.close()
