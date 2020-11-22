def prime_number_query(sNum, eNum):
    print("The prime number in %d~%d:\n"%(sNum,eNum))
    width = len(str(eNum))  # 取长度，作为输出数据的宽度
    count = 1
    for num in range(sNum, eNum + 1):  # 遍历判断num是否为素数
        if num == 1:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            print(format(num, "%dd" % width), end=' ')  # 格式化打印
            if count % 10 == 0:  # 10个数为一行，满10个换行
                print('')
            count += 1
    # else:
    #     print('\n')
    #     main()


def main():
    try:
        startingNum, endingNum = eval(input("Please enter an integer range(such as:1,100):"))  # 用户输入一个整数区间，例题为1~100
        if startingNum > 0 and endingNum > 0 and startingNum != endingNum:  # 判断输入数据是否符合要求
            if startingNum > endingNum:  # 如果起始数值大于终止数值，则互换
                startingNum, endingNum = endingNum, startingNum
            prime_number_query(startingNum, endingNum)  # 函数调用
        else:
            print("The input data dose not fulfil the requirements!")
    except:
        print("The input data dose not fulfil the requirements!")


if __name__ == "__main__":
    main()
