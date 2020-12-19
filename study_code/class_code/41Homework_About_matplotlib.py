# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @Time:    2020/12/11 16:32
# @File:    41Homework_About_matplotlib.py
# @Software:PyCharm


"""
使用matplotlib模块中的子模块pyplot模块绘制y=x^2和y=x^3的曲线
"""

import numpy as np  # 导入numpy模块，并重新命名为np
import matplotlib.pyplot as plt  # 导入matplotlib模块中的子模块pyplot，并重新命名为plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置rc参数显示中文字体，此处为：黑体
plt.rcParams["axes.unicode_minus"] = False  # 设置rc参数正常显示符号

data = np.arange(0, 1.1, 0.01)  # 创建一个从0到1.1步长为0.01的一维数组data
plt.title("曲线")  # 为图表添加标题为：曲线
plt.xlabel('x')  # 设置x轴的名称为：x
plt.ylabel('y')  # 设置y轴的名称为：y

plt.xticks([0, 0.5, 1.0])  # 设置x轴的刻度为：0，0.5，1.0
plt.yticks([0, 0.5, 1.0])  # 设置y轴的刻度为：0，0.5，1.0
plt.plot(data, data ** 2)  # 将数组data中的每个元素作为参数，绘制y=x^2的曲线
plt.plot(data, data ** 3)  # 将数组data中的每个元素作为参数，绘制y=x^3的曲线
plt.legend(["y=x^2", "y=x^3"])  # 为图表添加图例：y=x^2,y=x^3
plt.show()  # 显示图表
