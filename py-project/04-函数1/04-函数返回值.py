# 函数的返回值可以返回任意类型，返回值类型取决于return后面的类型


def getSum(a, b):
    return a + b


print(getSum(1, 6))


def getJieCheng(n):
    num = 1
    result = 1
    list = []
    while num <= n:
        result *= num
        list.append(num)
        num += 1
    # 可以返回多个值，返回的是一个元组
    return result, list


print(getJieCheng(5))
print(getJieCheng(5)[0])
print(getJieCheng(5)[1])
