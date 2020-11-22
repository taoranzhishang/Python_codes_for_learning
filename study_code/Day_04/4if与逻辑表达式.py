str = input("please input:")
# 关系运算符的结果使bool型
str1 = (str == "yes")  # 赋值一个逻辑表达式的结果，==为Ture；！=为False，str1是一个bool变量
if str1:
    print(str1)
print('a' == 'b')  # 直接比较，ture与false，输出bool型的结果
# if判断都是按照bool类型,None是假,通常赋值给一个不立即使用的变量，赋值的变量占位
# 空为false，0为false，非0为true
if 1:  # 非0为false
    print("true")
'''
if 0:#0为false
    print("false")
if '':#‘’，“”空为false
    print("true")
else:
    print("false")
if None:
    print("1")
'''
