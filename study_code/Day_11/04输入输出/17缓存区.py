# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    17缓存区.py
# @Time:    2020/12/13 23:09
# @Software:PyCharm

"""
python写入
实时写入
延时写入：write()先写入内存的缓冲区，没有实时写入，close()过后再从缓冲区写入磁盘
"""
import time

file = open(r"D:\code\py\study_code\Day_11\04输入输出\cache.txt", "wb")
file.write("你好天朝".encode("utf-8"))
file.flush()  # 刷新，实时写入
time.sleep(10)  # 不刷新会等带sleep(10)后关闭文件再写入磁盘
file.close()
