r = input("输入圆的半径")  # input输入的是字符串类型，计算不能直接使用
print(r, type(r))
r = eval(r)  # eval() 函数用来执行一个字符串表达式，并返回表达式的值
print(r ** 2 * 3.1415926)
