import pymysql

try:
    db = pymysql.connect("127.0.0.1", "root", "111111")
    cursor = db.cursor()  # 数据的游标
    # cursor.execute("SELECT VERSION()")#(('5.7.18-log',),)数据库类型
    cursor.execute("use  xiaomi")
    # cursor.execute("delete  from  leibusi  where  username='gaoqinghua'")删除
    # cursor.execute("insert into  leibusi values(1,'gaozhonghua',102323)")#增加
    cursor.execute("update  leibusi  set username='gaoqinghua'  where username='gaozhonghua'")
    db.commit()  # 生效
    db.close()
    print("密码正确")
except:

    print("密码错误")
