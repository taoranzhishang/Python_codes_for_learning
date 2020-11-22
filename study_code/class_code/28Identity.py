import datetime


def calBirthday(idNumber):
    birth = idNumber[6:14]
    birthday = datetime.datetime.strptime(birth, "%Y%m%d")
    print("你的出生日期为：{}".format(birthday))


def calGender(idNumber):
    if int(idNumber[-2]) % 2 == 1:
        print("你的性别是：男")
    else:
        print("你的性别是：女")


def calAge(idNumber):
    age = int(datetime.datetime.now().year - int(idNumber[6:10]))
    print("你的年龄为%d岁" % age)


def main():
    idNumber = input("请输入你的身份证号：")
    calBirthday(idNumber=idNumber)
    calGender(idNumber=idNumber)
    calAge(idNumber=idNumber)


if __name__ == "__main__":
    main()
