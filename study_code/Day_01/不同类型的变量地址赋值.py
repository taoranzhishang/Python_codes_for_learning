'''
python不同类型的变量可以赋值，地址赋值
原理是将各类型的常量的地址赋值给变量，而不是赋值的数据
'''

# a=10
# print(a)
# a=10.0
# print(a)
# a="你好"
# print(a)

a = 1
b = 1
print(id(a), id(b))
a = 100
b = 100
print(id(a), id(b))  # 多个数据逗号隔开
