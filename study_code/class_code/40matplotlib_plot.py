import matplotlib.pyplot as plt
import numpy as np
import math

# plt.figure(figsize=(20, 20), facecolor="gray", edgecolor="black")
# x = np.linspace(-np.pi, np.pi, 256)  # -pi~pi等分为256份
# c, s = np.cos(x), np.sin(x)  # 赋值，三角函数
# plt.plot(x, s, "m:")  # 品红短虚线
# plt.plot(x, c, "c--")  # 青色长虚线
# plt.savefig("1.png")  # 保存，默认路径为代码同路径

plt.figure(figsize=(20, 20), facecolor="gray", edgecolor="black")
# plt.axes()#参数取值0~1，y宽度，x宽度
axes1 = plt.subplot(3, 2, 1)
axes2 = plt.subplot(3, 2, 2)
axes3 = plt.subplot(3, 2, 3)
axes4 = plt.subplot(3, 2, 4)

x = np.arange(-10, 10, 0.01)
s = np.sin(x)
axes1.plot(x, s)

x = np.arange(-10, 10, 0.01)
s = np.cos(x)
axes2.plot(x, s)

x=np.arange(-10,10,0.01)
s=np.pie(x)
axes3.plot(x,s)

x=np.arange(-10,10,0.01)
s=np.math.cot(x)
axes4.plot(x,s)

plt.show()
