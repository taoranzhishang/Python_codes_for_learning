def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(5))
