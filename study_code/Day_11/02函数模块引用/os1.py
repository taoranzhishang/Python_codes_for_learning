# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    os1.py
# @Time:    2020/12/13 0:02
# @Software:PyCharm

"""
一个文件就是一个包
自己的文件不可以与系统文件重名
若根目录下有一个os.py
import os#根目录下，导入os实际导入的是自己
os.system("calc")
"""
import os  # 导入系统模块,此时若有一个自建的os.py1则会导入自建的os.py

os.system("calc")
