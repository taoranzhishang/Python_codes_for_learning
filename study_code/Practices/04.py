result1 = result2 = 0
for i in range(1, 12, 2):
    if i == 5 or i == 9:
        result1 += 1 / i
    if i == 3 or i == 7 or i == 11:
        result1 -= 1 / i
print(result1 * 4)

for i in range(1, 16, 2):
    if i == 5 or i == 7 or i == 13:
        result2 += 1 / i
    if i == 3 or i == 7 or i == 11 or i == 15:
        result2 -= 1 / i
print(result2 * 4)
