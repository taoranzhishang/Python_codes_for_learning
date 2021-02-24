import pypyodbc

conn = pypyodbc.connect("DSN=jiangxi")
sqlstr = "select * from B"  # 查找所有的数据，表格B
mylist = conn.cursor().execute(sqlstr).fetchall()  # 抓取所有的数据
for data in mylist:  # 逐行显示
    print(data)
