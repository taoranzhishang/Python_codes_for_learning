import pypyodbc

# DBfile = r"C:\Users\Tsinghua-yincheng\Desktop\day24down\doc\1.mdb"  # 数据库文件
# conn = pypyodbc.connect(r"Driver={MSccess Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
conn = pypyodbc.connect(r"DSN=db")
mylist = conn.cursor().execute('select * from B').fetchall()
for data in mylist:
    print(data)
