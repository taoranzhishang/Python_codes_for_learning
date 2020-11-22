'''
lambda表达式，函数
：左边为输入，右边为输出，函数后面是传的加参数

'''

num = lambda a, b: a + b

print(num(1, 2))

print((lambda a, b: a + b)(1, 2))

(lambda str: print(str))("hello world")
(lambda str1:repr(print(str1)))("hello world")
