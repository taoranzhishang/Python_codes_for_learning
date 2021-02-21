import telnetlib


def doTestuserpass(IP, user, password, command):
    try:
        tn = telnetlib.Telnet(IP)  # 链接服务器IP地址
        tn.set_debuglevel(2)  # 输入输出调试，设定级别2
        # tn.write("\r\n".encode("utf-8"))  #回车一次

        rt = tn.read_until("login:".encode("utf-8"))  # 读取到这个信息，没有读取到等待
        tn.write((user + "\r\n").encode("utf-8"))  # 输入用户名，回车

        rt = tn.read_until("password:".encode("utf-8"))  # 读取到这个信息，没有读取到等待
        tn.write((password + "\r\n").encode("utf-8"))  # 输入用户名，回车

        rt = tn.read_until(">".encode("utf-8"))  # 读到这个信息代表登陆成功
        tn.write((command + "\r\n").encode("utf-8"))  # 执行指令

        rt = tn.read_until(">".encode("utf-8"))
        tn.close()
        return True
    except:
        print("error")
        return False


if __name__ == "__main__":
    IP = "10.10.153.28"
    user = "administrator"
    password = "111111"
    command = "tasklist"
    print(doTestuserpass(IP, user, password, command))
