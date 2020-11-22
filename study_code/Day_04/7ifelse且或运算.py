a = 1
b = 1
c = 0

# and or都有短路效应；and优先级高于or
if a and b and c:  # and 且运算
    print("yes")
else:
    print("no")

if a or b and c:  # or 或运算
    print("yes")
else:
    print("no")

if a or c or c:  # or 或运算
    print("yes")
else:
    print("no")
