import telnetlib


def doTestuserpass(IP, user, password, command):
    try:
        tn = telnetlib.Telnet(IP)  # 链接服务器IP地址
        tn.set_debuglevel(2)  # 输入输出调试，设定级别2
        rt = tn.read_until("localhost login:".encode("utf-8"))  # 读取到这个信息，没有读取到等待
        tn.write((user + "\n").encode("utf-8"))  # 输入用户名，回车

        rt = tn.read_until("Password:".encode("utf-8"))  # 读取到这个信息，没有读取到等待
        tn.write((password + "\n").encode("utf-8"))  # 输入用户名，回车

        rt = tn.read_until("Login incorrect".encode("utf-8"), 5)
        if (rt.decode("utf-8")).find("Login incorrect") != -1:
            print("登陆失败")
            return False
        '''
        rt = tn.read_until("~]$".encode("utf-8"), 5)
        if (rt.decode("utf-8")).find("~]$")!=-1:
            print("登陆成功")
            return True
        '''

        # print("last",type(tn.read_all()),tn.read_all())
        print("登陆成功")
        return True
    except:
        print("error")
        return False


if __name__ == "__main__":
    IP = "10.10.153.29"
    user = "python"
    password = "111111"
    command = "mkdir fuck1"
    print(doTestuserpass(IP, user, password, command))
