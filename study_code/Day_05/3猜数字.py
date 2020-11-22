import random

num = random.randint(1, 100)
num1 = eval(input("please input a number:"))
while num != num1:
    if num < num1:
        print("big")
    else:
        print("small")
    num1 = eval(input("please input a num again:"))
else:
    print("right")
