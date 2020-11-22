num1, num2, num3, num4 = 1, 2, 3, 4

'''
执行满足条件的语句，后面不执行
'''
if num1 == 1:
    print(num1)
elif num2 == 2:
    print(num2)
elif num3 == 3:
    print(num3)
elif num4 == 4:
    print(num4)
else:
    pass
'''
if嵌套满足向下执行，不满足不执行
'''
if num1 == 0:
    print(num1)
    if num2 == 2:
        print(num2)
        if num3 == 3:
            print(num3)
        else:
            print('?')
    else:
        print('?')
else:
    print('?')
