def fun1(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        data = True
        for i in range(2, num):
            if num % i == 0:  # 有一个可以整除，则不是,并跳出循环
                data = False
                break
        return data


def fun2(num):
    for i in range(1, num):
        if fun1(i) and fun1(num - i):  # 判断i和num-i两个数都是质数
            print(num, '=', i, '+', num - i)


for i in range(100, 150):
    fun2(i)
