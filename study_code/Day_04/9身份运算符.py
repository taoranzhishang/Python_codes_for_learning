num1 = 1
num2 = 2

'''
关系运算 身份运算符is ,is not表示是和不是
x is y-->id(x)h==id(y)
x is not y-->id(x)h!=id(y)
区别：is比较x，y引用的对象是否是同一个，==比较值使否相等
'''
if num1 is num2:
    print('=')
else:
    print('!=')
