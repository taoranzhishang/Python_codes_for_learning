'''
有bug
'''
a, b, c = eval(input("依次输入a,b,c:"))
print("%dx^2+%dx+%d"%(a,b,c))
if a == 0:
    if b == 0:
        if c == 0:
            print("x为任意值")
        else:
            print("方程无解")
    else:
        print("x=", c / b)
else:
    dt = b ** 2 - 4 * a * c
    print("dt=%d"%dt)
    if dt == 0:
        print("x=", (-1 * b + dt ** 0.5) / (2 * a))
    elif dt > 0:
        print("x1=", (-1 * b + dt ** 0.5) / (2 * a), "\n", "x2=", (-1 * b - dt ** 0.5) / (2 * b))
    else:
        print("dt<0,方程无实根")
