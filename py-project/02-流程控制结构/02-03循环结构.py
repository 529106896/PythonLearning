# 两种循环：
# while、for
# tmp = 1
# while tmp <= 100:
#     print(tmp)
#     tmp += 1

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%2d\t" % (j, i, i * j), end='')  # 使用end不让print换行
        j += 1
    i += 1
    print()
