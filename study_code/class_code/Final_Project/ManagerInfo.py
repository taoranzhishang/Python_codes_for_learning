# -*-coding:utf-8-*-
# @Author:  陶然至上
# @Email:   taoranzhishang@hotmail.com
# @File:    ManagerInfo.py
# @Time:    2020/12/16 19:06
# @Software:PyCharm
import pandas as pd


def register():
    """
    用户注册
    用户键盘输入用户名userName和用户密码userPassword，并存储于userData中
    将userData以2进制方式写入users.txt文件
    注册成功调用登录寒暑Login()，注册失败则调用注册函数重新注册
    """
    print("----用户注册----")
    flag = False
    while True:
        userName = input("请输入用户名：")
        usersFile = open("../info/users.txt", "a+")
        info = usersFile.readlines()
        for data in info:
            if data != None:
                if userName == (eval(data))["name"]:
                    print("用户名已存在，请重新输入")
                    usersFile.close()
                    register()
            else:
                usersFile.close()
                break
        else:
            userPassword = input("请输入初始密码：")
            usersFile = open("../info/users.txt", "a+")
            userData = {"name": userName, "pwd": userPassword}
            usersFile.write(str(userData) + "\r")
            usersFile.close()
            flag = True
            break
    if flag:
        Login()
    else:
        print("注册未成功，请重新注册")
        register()


def Login():
    """
    用户登录函数
    先判断用户输入的用户名是否存在，若存在判断用户输入的密码是否与用户名的密码对应
    密码对应登录成功，调用ReadCVS()函数，密码不对应提示登录失败，重新调用登陆函数重新登录
    """
    print("----用户登录----")
    userName = input("请输入用户名：")
    usersFile = open("../info/users.txt", "r")
    info = usersFile.readlines()
    flag = True
    for data in info:
        if data != None:
            userData = eval(data)
            if userName == userData["name"]:
                flag = False
                userPwd = input("请输入登录密码：")
                if userPwd == userData["pwd"]:
                    print("登陆成功")
                    ReadCSV()
                else:
                    print("登陆失败，请重新登录")
                    Login()
            else:
                continue
        else:
            print("数据加载出现问题")
            break
    if flag:
        print("该用户名还未注册")
        ts_loginPrint()


def ReadCSV():
    """
    将数据写入文件Student.CSV，并读取打印该文件
    然后向Student.CSV文件中添加新的一列result
    """
    userDF = pd.DataFrame([[202001, "张三", 18], [202002, "李四", 20]],
                          columns=["sno", "sname", "sage"])
    userDF.to_csv("../info/Student.csv")
    print("CSV文件数据为：")
    data = pd.read_csv("../info/Student.csv", index_col=0)
    print(data)
    data["result"] = pd.Series([86, 87])
    data.to_csv("../info/Student.csv")


def ts_loginPrint():
    """
    用户注册登录选择
    输入1调用register()进行注册：输入2调用Login进行登录
    """
    while True:
        print("请问您先注册还是登录（注册：1，登录：2）：")
        userSelect = input("请输入1或者2：")
        if userSelect == '1':
            register()
            break
        elif userSelect == '2':
            Login()
            break
        else:
            print("您的输入不符合系统要求，请重新输入")
