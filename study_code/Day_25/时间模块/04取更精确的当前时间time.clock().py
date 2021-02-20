import time

start = time.clock()
num = 0
for i in range(10000):
    num += i
end = time.clock()
print(end - start)
