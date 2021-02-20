import datetime
import time

# print(dir(datetime))
"""
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 
 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

# print(datetime.datetime.now())  # 2021-02-20 16:46:33.886215
start = datetime.datetime.now()  # 2021-02-20 16:49:57.812746
time.sleep(3)
end = datetime.datetime.now()  # 2021-02-20 16:50:00.813804
print(start)
print(end)
print(end - start)  # 0:00:03.000130 时间差

end = datetime.datetime(2022, 2, 20, 5, 20, 13, 14)  # 构造时间
print(end)
print(end - start)  # 364 days, 12:27:03.360143

print((end - start).days)  # 364，取天数
print((end - start).seconds)  # 44405，时分秒转换为秒

start = datetime.date(2021, 2, 20)  # 2021-02-20
end = datetime.date(2022, 2, 20)  # 2022-02-20
print(start)
print(end)
print(end - start)  # 365 days, 0:00:00
print(start - end)  # -365 days, 0:00:00

start = datetime.datetime.strptime("2021-02-20 05:20:13", "%Y-%m-%d %H:%M:%S")
end = datetime.datetime.strptime("2022-02-20 05:20:13", "%Y-%m-%d %H:%M:%S")
print(start)  # 2021-02-20 05:20:13
print(end)  # 2022-02-20 05:20:13
print(end - start)  # 365 days, 0:00:00
print(type(start))  # <class 'datetime.datetime'>
print(datetime.datetime.strftime(start, "%Y-%m-%d %H:%M:%S"))
print(type(datetime.datetime.strftime(start, "%Y-%m-%d %H:%M:%S")))  # <class 'str'>
