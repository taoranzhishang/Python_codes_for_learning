# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    44test.py
# @Time:    2020/12/16 17:12
# @Software:PyCharm
import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([1, 5, 8, 8,
                            2, 2, 4, 9,
                            7, 4, 2, 3,
                            3, 0, 5, 2]).reshape(4, 4), columns=['A', 'B', 'C', 'D'])
print(df)
df.to_csv(r"D:\code\py\study_code\class_code\test.csv")

data = pd.read_csv(r"D:\code\py\study_code\class_code\test.csv", header=0, index_col=0)
print(data)
