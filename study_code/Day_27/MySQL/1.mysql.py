import pymysql

try:
    db = pymysql.connect("127.0.0.1", "root", "111111")
    cursor = db.cursor()  # 数据的游标
    # cursor.execute("SELECT VERSION()")#(('5.7.18-log',),)数据库类型
    cursor.execute("use  xiaomi")
    cursor.execute("show  tables")
    data = cursor.fetchall()  # 查询的结果
    print(data)
    db.close()
    print("密码正确")
except:

    print("密码错误")
