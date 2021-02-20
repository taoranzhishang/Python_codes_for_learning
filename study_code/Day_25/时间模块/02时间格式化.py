import time

print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=20, tm_hour=16, tm_min=9, tm_sec=45, tm_wday=5, tm_yday=51, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2021-02-20 16:09:45
print(time.strftime("%Y--%m--%d %H::%M::%S", time.localtime()))  # 2021--02--20 16::12::13
print(time.strftime("%Y year %m month %d day %H hour %M minutes %S second", time.localtime()))  # 只能符号和字母，不能用汉字
# 2021year02month20day 16hour:13minutes:29second
myStr = "2021-02-20 16:14:09"
myTime = time.strptime(myStr, "%Y-%m-%d %H:%M:%S")  # 符号必须匹配才能转换
print(myTime)
# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=20, tm_hour=16, tm_min=14, tm_sec=9, tm_wday=5, tm_yday=51, tm_isdst=-1)
print(type(myTime))  # <class 'time.struct_time'>
print(time.mktime(myTime))  # 1613808849.0 距其实时间的时间
