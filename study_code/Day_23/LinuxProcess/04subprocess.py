import subprocess

pingP = subprocess.Popen(args=["gedit"], shell=True)  # 执行外部程序与shell
pingP.wait()  # 等待
print(pingP.pid)  # 打印编号
print(pingP.returncode)  # 返回值
