num = 1
myStr = "abc"
"""
isintance()判断一个对象与类的类型是否相同，子类是否属于父类
type()是对类型严格检查
"""
print(type(int), type(num))  # <class 'type'> <class 'int'>
print(isinstance(num, int))  # True
print(isinstance(num, str))  # False
print(isinstance(myStr, str))  # True
print(isinstance(myStr, int))  # False
print(isinstance(num, (str, int, float)))  # True，元组内的其中一个满足即可
print(isinstance(num, (str, float)))  # False


class Father:
    pass


class Kid(Father):
    pass


print(type(Father()) == Father)  # True，type()只能处理对象，
print(isinstance(Father(), Father))  # True，匿名对象与类的类型是否相同
print(isinstance(Father, Father))  # False，isinstance是判断一个对象与一个类的类型是否相同
print(isinstance(Kid(), Father))  # True，子类匿名对象与父类类型
