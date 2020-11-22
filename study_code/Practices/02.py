import math

print("a    a^2   a^3")
for i in range(1, 5):
    print(i, end='')
    for j in range(2, 4):
        print("   ", format(pow(i, j), ">2d"), end='')
    print("")
