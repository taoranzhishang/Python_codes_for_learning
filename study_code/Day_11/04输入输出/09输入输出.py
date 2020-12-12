# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    09输入输出.py
# @Time:    2020/12/13 0:51
# @Software:PyCharm

myStr = "hello python\n"
print(myStr)  # 转换为人供人读取的形式，hello python[\n]

print(repr(myStr))  # 转换为供解释器读取的形式,'hello python\n'不换行，可以观察转义字符

data = 3 / 7
print(str(data))  # 0.42857142857142855#一般数据二者相同
print(repr(data))  # 0.42857142857142855
"""
repr可处理任何类型的数据，可标识类型
str不能标识类型，统一转换为str
"""
print(repr(str))  # <class 'str'>
print(repr(int))  # <class 'int'>
print(repr('1'))  # '1'
print(repr(1))  # 1
print(str('1'))  # 输出1，不能识别类型
print(str(1))  # 输出1，不能识别类型

print('1', '2')
print('1'.rjust(10), '2')  # rjust调整字符串左边宽度
print('1'.ljust(10), '2')  # ljust调整字符串右边宽度

for x in range(100):
    print(repr(x).rjust(10), repr(x * x).rjust(10), repr(x * x * x).rjust(10))
