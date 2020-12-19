# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    45数据获取.py
# @Time:    2020/12/16 17:34
# @Software:PyCharm
import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([1, 5, 8, 8,
                            2, 2, 4, 9,
                            7, 4, 2, 3,
                            3, 0, 5, 2]).reshape(4, 4), columns=['A', 'B', 'C', 'D'])
print(df)
# df.to_csv("test.csv")
# data = pd.read_csv("test.csv", header=0, index_col=0)
# print(data)
print(df['A'])  # 取A索引的行
data = df.values[0]  # 获取df的值，取第0行
print(data)
"""
添加数据
"""
df['D'] = pd.Series([1, 2, 3, 4, 5])
print(df)
