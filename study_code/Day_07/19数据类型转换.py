print(int("123"))  # str转int
print(str(123))  # int转str
print(float("12.234"))  # str转float

print(tuple([1, 2, 3, 4]))  # list转tuple
print(tuple({1, 2, 3, 4}))  # set转tuple

print(list((1, 2, 3, 4)))  # tuple转list
print(list({1, 2, 3, 4}))  # set转list

print(set((1, 2, 3, 4)))  # tuple转set
print(set([1, 2, 3, 4]))  # list转set

print(repr(1 + 2 * 3))  # 计算一个表达式，运算
print(repr("1+2*3"))  # 计算一个表达式，字符串

print(int("16",2))
print(bin(16))  # 2进制

print(int("16", 8))  # 8进制
print(oct(16))

print(int("16", 10))  # 10进制

print(int("16", 16))  # 16进制
print(hex(16))
