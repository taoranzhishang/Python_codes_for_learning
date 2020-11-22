import time

# import random

time_data = time.time()
print(time_data)
print(type(time_data))  # flaot类型
time_data = int(time_data) % 26

# time_data=random.randint(0,26)

print("小写", chr(ord('a') + time_data))
print("大写", chr(ord('A') + time_data))
