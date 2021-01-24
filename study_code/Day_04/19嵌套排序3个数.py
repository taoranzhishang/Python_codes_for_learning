a, b, c = eval(input("please input 3 numbers:"))
print('0:',a, b, c)
if a < b:
    # a, b = b, a
    print('1:',a, b, c)

    a ^= b
    b ^= a
    a ^= b
if a < c:
    # a, c = c, a
    print('2:',a, b, c)

    a ^= c
    c ^= a
    a ^= c
if b < c:
    # b, c = c, b
    print('3:',a, b, c)

    b ^= c
    c ^= b
    b ^= c

print('4:',a, b, c)
