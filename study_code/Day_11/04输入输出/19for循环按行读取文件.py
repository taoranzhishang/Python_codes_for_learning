# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    19for循环按行读取文件.py
# @Time:    2020/12/13 23:37
# @Software:PyCharm
filePath = "D:\\code\\py\\study_code\\Day_11\\04输入输出\\text.txt"
file = open(filePath, 'rb')
"""
'r'直接读取，会处理文本中的换行符，输出是会对文本中的换行符换行
"rb"按照二进制读取，文本中的换行符会以二进制形式读取，不会换文本中的换行，若要处理，需要decode()解码
"""
for line in file:  # file是每一行数据的集合
    print(line.decode("utf-8"))
file.close()
