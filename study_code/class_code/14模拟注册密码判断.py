def pwdCheck(str):
    # 两个都不满足用or，只能一个满足用and
    strFormat = (not (str.isalpha() or str.isdigit()) and str.isalnum())
    length = len(str)
    formatData = False
    lengthData = False

    if strFormat != True:
        print("请输入数字、字母组成的密码！")
    else:
        formatData = True

    if length < 8 or length > 20:
        print("请输入8-20位密码！")
    else:
        lengthData = True

    if formatData and lengthData:
        tempStr = str
        for line in tempStr:
            newStr = tempStr.replace(line, '.')
            tempStr = newStr
        print(tempStr)
        print('{:#^25}'.format(str))

    # if strFormat!=True:
    #     print("请输入数字、字母组成的密码！")
    # else:
    #     if length<8 or length>10:
    #         print("请输入8-20位密码！")
    #     else:
    #         tempStr = str
    #         for line in tempStr:
    #             newStr = tempStr.replace(line, '.')
    #             tempStr = newStr
    #         print(tempStr)
    #         print('{:#^25}'.format(str))


while True:
    password = (input("请输入您的密码："))
    pwdCheck(password)
