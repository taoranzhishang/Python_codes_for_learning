# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    46读取文件添加数据.py
# @Time:    2020/12/16 17:55
# @Software:PyCharm

import pandas as pd

data = pd.read_csv("demo.csv", index_col=0)
print(data)
data["col4"] = pd.Series([1,3])#使用列表,元组
print(data)
