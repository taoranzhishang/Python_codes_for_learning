import pymysql  # 安装  pip  install  pymysql

try:
    db = pymysql.connect("127.0.0.1", "root", "111111a")
    db.close()
    print("密码正确")
except pymysql.err.OperationalError:
    print("密码错误")
else:
    # 用于处理正确的结果
    print("没有错误的时候执行")
