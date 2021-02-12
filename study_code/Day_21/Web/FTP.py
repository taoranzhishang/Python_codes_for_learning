# http://hk801.pc51.com/  破解FTP密码


'''
"user"
csdn  user用户名

密码字典  password

'''
import ftplib

try:
    myftp = ftplib.FTP("hk801.pc51.com")  # 登陆服务器
    myftp.login("qinghuabeidacn517", "yinchengak47")
    print("密码正确")
except:
    print("密码不正确")
