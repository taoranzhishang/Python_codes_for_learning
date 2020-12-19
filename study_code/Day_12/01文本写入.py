# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    01文本写入.py
# @Time:    2020/12/14 19:25
# @Software:PyCharm
file=open(r"D:\code\py\study_code\Day_12\text.txt","w")
myStr="Hello China 你好天朝"#字符串，默认编码utf-8
file.write(myStr)#系统自动指定，默认中文环境为GBK
file.close()