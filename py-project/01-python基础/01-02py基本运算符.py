'''
基本运算符有：
加法 +
减法 -
乘法 *
求指数 **
取余 %
除法 /
整除 //
'''
a = 7
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a**b)
print(a % b)
print(a / b)
print(a // b)

'''
比较运算符有：
等于 ==
不等于 !=
大于 >
小于 <
大于等于 >=
小于等于 <=
'''
# 介绍一个简单的赋值方法
a, b = 10, 5
print(a > b)

'''
逻辑运算符有：
且 and
或 or
取反 not
优先级是：括号——取反——且——或
'''
print(True and False)
print(True or False)
print(False or True)
print(not True)
print(True or True and False or False and False)  # 相当于(True) or (True and False) or (False and False)


'''
赋值运算符有：
赋值 =
加法赋值 +=
减法赋值 -=
乘法赋值 *=
除法赋值 /=
取模赋值 %=
幂等赋值 **=
整除赋值 //=
'''
tmp = 1
# print(tmp += 1) 注意这样会报错，因为+=是一个复合的表达式，不能直接打印
tmp += 1
print(tmp)
