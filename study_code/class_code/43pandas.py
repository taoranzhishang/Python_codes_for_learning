# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    43pandas.py
# @Time:    2020/12/16 16:18
# @Software:PyCharm


import pandas as pd
import numpy as np

"""
Series 一维数据
列表、一维数组、元组、字典做参数
"""
Ser1 = pd.Series([1, 3, 5], index=["l1", "l2", "l3"])  # 生成一个Series对象，行标签
print(Ser1)
arr = np.arange(1, 101)  # 生成一维数组，作为参数
Ser2 = pd.Series(arr)  # 生成7行
print(Ser2)
Ser3 = pd.Series({'a': 1, 'b': 2, 'c': 3})  # dict为参数，行标签为key
print(Ser3)

"""
DataFrame 二维数据
可用二维数组、字典、Series对象，DataFrame对象做参数
"""
df = pd.DataFrame(np.arange(1, 7).reshape(2, 3), index=["l1", "l2"], columns=["col1", "col2", "col3"])
print(df)
print(df.values)
print(df.index)
print(df.columns)
"""
保存DataFrame对象至文件
"""
df.to_csv("demo.csv", mode='w')
data = pd.read_csv("D:\code\py\study_code\class_code\demo.csv", header=0, index_col=0, prefix='*')
print(data)
