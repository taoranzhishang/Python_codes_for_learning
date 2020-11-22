a, b, c = eval(input("please input 3 numbers:"))
print(a, b, c)
if a < b:
    # a, b = b, a
    print(a, b, c)

    a ^= b
    b ^= a
    a ^= b
if a < c:
    # a, c = c, a
    print(a, b, c)

    a ^= c
    c ^= a
    a ^= c
if b < c:
    # b, c = c, b
    print(a, b, c)

    b ^= c
    c ^= b
    b ^= c

print(a, b, c)
