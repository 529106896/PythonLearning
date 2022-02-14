sum1 = sum(range(1, 11))
print(sum1)

sum2 = sum(range(20, 31))
print(sum2)

ansArr = []

for i in range(1, 101):
    bigMonk = i
    smallMonk = 100 - i
    if 3 * i + smallMonk // 3 == 100:
        ansArr.append({"big": bigMonk, "small": smallMonk})

print(ansArr)

li = [1, 3, 4, 3, 2, 2, 5, 6, 6, 5, 7, 7, 3]
set1 = set(li)
print(set1)
for i in set1:
    li.remove(i)
print(li)
