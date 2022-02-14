'''
常用的有：
abs 绝对值
round 四舍五入
pow 求幂运算
divmod 求余和商
max
min
sum
eval 动态计算
'''

print(abs(-10))

# 四舍五入round，可规定保留几位小数
print(round(2.5))
print(round(2.578, 2))
print(round(2.578, 1))

# 求幂运算pow
print(pow(3, 3))

# 求商和余数
print(divmod(13, 3))

# 求最大值
print(max(1, 3, 5, 723, -324, 324, 2, 3225446, 457, 45, 634))
print(max([1, 23, 12345, 2345, 34, 64, 587, 456, 6523, 534, 7, 45]))

# 求和(最多只能有两个参数)
# print(sum(1, 2, 3, 4, 5, 6)) 这个是错误的
print(sum([1, 2, 3]))
print(sum([4, 1, 2, 3], 7))  # 第二个参数用于指定求完和之后再加上多少

# 动态执行表达式eval
print(eval("1 + 2"))
a, b, c = 1, 2, 3
print(eval('a+b+c'))
print(eval("num1 + num2", {"num1": 1, "num2": 2}))  # 可以直接用字典为变量赋值


def testEval():
    print("running testEval")
    pass


eval("testEval()")  # 可用于执行函数
