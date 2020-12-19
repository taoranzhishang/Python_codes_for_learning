# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    02文本读取中文编码常见错误.py
# @Time:    2020/12/14 19:27
# @Software:PyCharm
"""
#bug已修复
file=open("D:\\code\\py\\study_code\\Day_12\\text.txt","w")
myStr="Hello China 你好天朝"#字符串，默认编码utf-8
file.write(myStr)#系统自动指定，默认中文环境为GBK、ANSI，可能会编码不对应，编码错误
file.close()
"""
"""
实际开发中读写应使用自己指定的编码方式，2进制读写，易于迁移，不推荐默认编码
window10默认编码ANSI,写入的时候ANSI
read()无法指定解码方式，只能按系统的ANSI
"""
file = open(r"D:\code\py\study_code\Day_12\text.txt", "r")
myStr = file.read()  # 不指定，按照系统默认编码法师编码，默认utf-8文件的utf-8与字符串的utf-8不是一个概念
print(myStr)
file.close()
