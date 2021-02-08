def func(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return func(num - 1) + func(num - 2)


print(func(25))
