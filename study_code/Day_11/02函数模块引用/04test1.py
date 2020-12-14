# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    04test1.py
# @Time:    2020/12/12 23:24
# @Software:PyCharm
"""
import 02函数模块引用.funcTest

02函数模块引用.funcTest.go()
"""
"""
import funcTest

funcTest.go()
"""
"""
from funcTest import go#from路径导入，调用函数时可以直接用，同命的后面的覆盖前面导入的
go()
"""
"""
import study_code.Day_11.04funcTest#直接import导入调用函数时要加路径
import study_code.Day_11.05funTest2
study_code.Day_11.funcTest.go()#函数调用
study_code.Day_11.funTest2.go()#不同路径下的同名函数不会重命名错误
"""
