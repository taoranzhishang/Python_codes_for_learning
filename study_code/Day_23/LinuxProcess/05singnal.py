import subprocess
import signal


def itout(signum, frame):  # 函数挂接信号
    print("signal is  end")


signal.signal(signal.SIGINT, itout)  # 意外中断启动函数itout

pingP = subprocess.Popen(args=["ping www.baidu.com"], shell=True)  # run shell
pingP.wait()
print(pingP.pid)
print(pingP.returncode)
