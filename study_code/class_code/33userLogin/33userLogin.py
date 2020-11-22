import os


def c_flag():
    '''
    登录信息初始化
    '''
    file = open("flag", 'w')
    file.write('1')
    file.close()


def init():
    '''
    创建用户文件
    '''
    file = open("u_root", 'w')
    root = {"rnum": "root", "rpwd": "123456"}
    file.write(str(root))
    file.close()
    os.mkdir("users")


def print_login_menu():
    '''
    打印登陆菜单
    '''
    print("----用户选择----")
    print("1-管理员登陆")
    print("2-普通用户登录")
    print("---------------")


def user_select():
    '''
    用户登录选择
    '''
    while True:
        user_type_select = input("请选择用户类型：")
        if user_type_select == '1':
            root_login()
            break
        elif user_type_select == '2':
            while True:
                select = input("是否需要注册？（y/n）")
                if select == 'y' or select == 'Y':
                    print("----用户注册----")
                    user_register()
                    break
                elif select == 'n' or select == 'N':
                    print("----用户登录----")
                    break
                else:
                    print("输入有误，请重新选择")
            user_login()
            break
        else:
            print("输入有误，请重新选择")


def root_login():
    '''
    管理员登陆
    '''
    while True:
        print("****管理员登陆****")
        root_number = input("请输入账户名：")
        root_password = input("请输入密码：")
        file_root = open("u_root")
        root = eval(file_root.read())
        if root_number == root["rnum"] and root_password == root["rpwd"]:
            print("登录成功！")
            break
        else:
            print("登陆失败！")


def user_register():
    '''
    普通用户注册
    '''
    user_id = input("请输入账户名：")
    user_pwd = input("请输入密码：")
    user_name = input("请输入昵称：")
    user = {"u_id": user_id, "u_pwd": user_pwd, "u_name": user_name}#写入id，密码，用户名
    user_path = "./users/" + user_id#同目录下创建users/user_id的路径
    file_user = open(user_path, 'w')#打开文件夹，没有则新建文件
    file_user.write(str(user))#写入数据
    file_user.close()


def user_login():
    '''
    普通用户登录
    '''
    while True:
        print("****普通用户登录****")
        user_id = input("请输入账户名：")
        user_pwd = input("请输入密码：")
        # 获取user目录中所有的文件名
        user_list = os.listdir("./users")
        # 遍历列表，判断user_id是否在列表中
        flag = 0
        for user in user_list:
            if user == user_id:
                flag = 1
                print("登陆中···")
                # 打开文件
                file_name = "./users/" + user_id
                file_user = open(file_name)
                # 获取文件内容
                user_info = eval(file_user.read())
                if user_pwd == user_info["u_pwd"]:
                    print("登陆成功！")
                    break
                else:
                    print("密码错误！")
                    break
        if flag == 1:
            break
        elif flag == 0:
            print("查无此人！请先注册用户")
            break


def main():
    flag = open("flag")
    word = flag.read()
    if word == '0':
        print("首次启动！")
        flag.close()
        c_flag()
        init()
        print_login_menu()
        user_select()
    elif word == '1':
        print("欢迎回来！")
        print_login_menu()
        user_select()
    else:
        print("初始化参数错误！")


if __name__ == "__main__":
    main()
