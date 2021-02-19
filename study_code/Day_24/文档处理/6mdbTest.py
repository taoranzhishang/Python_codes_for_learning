import win32com
import win32com.client

# 获取Connection对象
conn = win32com.client.Dispatch('ADODB.Connection')
# 设置ConnectionString
mdb_file = r"C:\Users\Tsinghua-yincheng\Desktop\day24down\doc\1.mdb"
conn.ConnectionString = "DSN = 'PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=C:\\Users\\Tsinghua-yincheng\\Desktop\\day24down\\doc\\江西122W移动全球通.mdb"  # mdb_file为mdb文件的路径

# 打开连接
conn.Open()  # 这里也可以conn.Open(DSN) DSN内容和ConnectionString一致
