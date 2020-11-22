def show(num1, num2, num3):
    print(num1, num2, num3)


show(1, 2, 3)  # 位置参数，默认顺序传入
show(num3=1, num1=3, num2=2)  # 名称参数，可以乱序

'''
print(1,end="")#名称参数
'''
