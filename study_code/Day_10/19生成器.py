# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    19生成器.py
# @Time:    2020/12/12 17:41
# @Software:PyCharm

myList = [x for x in range(1000)]  # []返回l类型为ist列表生成式，占内存，速度慢
print(myList, type(myList))

"""
函数外生成器--生成器表达式
generator,用一个生成一个，节约内存，构造表达式换成[]
区别：
构造表达式[]、生成器表达式()
"""

myGenerator = (x for x in range(1000000))  # ()返回类型为生成器
print(myGenerator)  # <generator object <genexpr> at 0x00000266C7EF3890>
print(type(myGenerator))  # <class 'generator'>
print(next(myGenerator))  # 0
print(next(myGenerator))  # 1
print(next(myGenerator))  # 2

"""
用于循环，节约内存
"""
for num in myGenerator:#遍历迭代
    print(num)
