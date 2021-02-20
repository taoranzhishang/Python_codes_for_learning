import time

tick = time.time()  # 1970.01.01 00:00到现在的时间
print(tick)
localTime = time.localtime(tick)
print(localTime)  # 格式化为本地时间，返回一个元组
# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=20, tm_hour=15, tm_min=56, tm_sec=55, tm_wday=5, tm_yday=51, tm_isdst=0)
print(type(localTime))  # <class 'time.struct_time'>
print(localTime[0], localTime[1])  # 2021 2
actTime = time.asctime(localTime)
print(actTime)  # Sat Feb 20 16:04:48 2021
print(type(actTime))  # <class 'str'>
