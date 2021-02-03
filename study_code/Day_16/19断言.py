def add(num1, num2):
    assert (type(num1) == type(num2)), "类型不同"  # 表达式1条件满足正常执行，否则报表达式2
    print(num1 + num2)


# add(1,'a')
add(1, 2)
