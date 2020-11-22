def prime_number_calc(beginningNum, endingNum):
    print("区间[%d,%d]内的素数有:\n"%(beginningNum,endingNum))
    width = len(str(beginningNum))
    counter = 1
    for num in range(beginningNum, endingNum + 1):
        if num == 1:
            continue
        for data in range(2, num):
            if num % data == 0:
                break
        else:
            print(format(num, "%dd" % width), end=' ')
            if counter % 10 == 0:
                print('')
            counter += 1


beginningNum, endingNum = eval(input("请输入一个整数区间:"))
if beginningNum > 0 and endingNum > 0 and beginningNum != endingNum:
    if beginningNum > endingNum:
        beginningNum, endingNum = endingNum, beginningNum
    prime_number_calc(beginningNum, endingNum)
else:
    print("您输入的数据不符合要求哦!")

