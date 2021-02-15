import time
import threadpool  # 库不成熟

"""
线程池的使用前提，线程没有冲突，库默认没有冲突
"""


def show(str):
    print("hello", str)
    time.sleep(2)


namelist = ["高清化", "hefengcheng", "sunyu", "gogog"]
start_time = time.time()  # 开始时间

pool = threadpool.ThreadPool(10)  # 最大容量10个
requests = threadpool.makeRequests(show, namelist)  # 设置参数，函数，参数列表
for req in requests:  # 遍历每一个请求，并开始执行
    pool.putRequest(req)  # 压入线程池开始执行

end_time = time.time()  # 结束时间
print(end_time - start_time)

'''
def  show(str):
    print("hello",str)
    time.sleep(2)

namelist=["高清化","hefengcheng","sunyu","gogog"]

start_time=time.time() #开始时间
for  name  in namelist:
    show(name)
end_time=time.time() #结束时间
print(end_time-start_time)

'''
