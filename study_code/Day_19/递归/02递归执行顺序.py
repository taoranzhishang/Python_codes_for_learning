def func(num):
    if num == 0:
        return
    else:
        print(num - 1)
        func(num - 1)
        print(num - 1)


func(5)
