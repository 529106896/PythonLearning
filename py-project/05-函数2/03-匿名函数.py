'''
py中使用lambda关键字创建匿名函数
匿名函数即这个函数没有名字，不用def创建
语法：lambda 参数1,参数2,参数3...参数n:执行表达式
自带return，return的结果是表达式计算之后的结果
如：
test = lambda x,y:x+y
test(1,3)
test(4,5)
转换成普通函数：
def test(x,y):
    return x+y

匿名函数的缺点：lambda只能是单个表达式，不是代码块，因为lambda的设计就是为了满足简单的函数，仅能封装有限的逻辑
'''


def compute(x, y):
    return x + y


test = lambda x, y: x + y
print(compute(10, 5))
print(test(1, 4))

result = lambda a, b, c: a * b * c
print(result(3, 4, 5))
'''
py中的三元运算：
if a:
    b
else:
    c
可以转换成：
b if a else c

可以与lambda结合来实现选择逻辑
'''
a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
print("二者较大的是{}".format(b if b > a else a))

# 与lambda结合
funcTest = lambda x, y: x if x > y else y
print("The bigger one is %d" % funcTest(1, 6))

# lambda直接调用
funcTest1 = (lambda x, y: x if x > y else y)(7, 8)
print(funcTest1)
