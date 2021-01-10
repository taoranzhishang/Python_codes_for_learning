# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    04邮箱提取.py
# @Time:    2021/1/9 10:36
# @Software:PyCharm

filepath = r"D:\code\py\study_code\Day_12\demo.txt"
file = open(filepath, "rb")  # 读取结果为二进制

useremail_filepath = r"D:\code\py\study_code\Day_12\email.txt"
useremail_file = open(useremail_filepath, "wb")

for data in file:  # 遍历数据
    # print(data)#以"wb"方式打开，结果为二进制
    data = data.decode("utf-8", "ignore")  # 对数据解码，方式为utf-8，忽略错误
    filestr = data.split(" # ")  # 切割每一行
    # print(filestr[2],end='')
    useremail_file.write(filestr[2].encode("utf-8"))  # 将邮箱数据写入文件，编码方式utf-8

file.close()
useremail_file.close()
