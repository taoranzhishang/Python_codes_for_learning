# func = (lambda x: x % 2 == 1)
# print(func(1))
# print(func(2))


myList1 = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]))
print(myList1)  # [1, 3, 5]


def func(x):
    return x % 2 == 1


myList2 = list(filter(func, [10, 204, 50, 41, 1]))
print(myList2)  # [41, 1]
