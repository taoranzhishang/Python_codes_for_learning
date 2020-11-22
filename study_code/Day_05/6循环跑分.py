import time

startTime = time.time()
end_num = 0
for i in range(100000000):
    end_num += 1
endTime = time.time()

print(end_num)
print(endTime - startTime)
'''
for效率高于while
while适合死循环
'''
