'''
参数分类：
必选参数、默认参数(缺省参数)、可选参数、关键字参数
'''

# 必选参数：调用的时候必须给他赋值


def getSum(a, b):
    print(a + b)
    pass


getSum(2, 4)

# 默认参数：也叫缺省参数
# 注意：默认参数必须要在参数列表尾部，后面不能再有必选参数
# 比如不能有 def function(a, b=40, c):


def getSum1(a=10, b=60):
    print(a * b)
    pass


getSum1(1)

# 可选参数：也叫不定长参数，当参数个数不确定时使用，用*来代替(最好放在尾部)


def getSum2(a, b, *args):
    '''
    计算累加和
    '''
    print(a)
    print(b)
    for i in args:
        print(i, end=" ")
        pass
    print()
    pass


getSum2(1, 2, 3, 4, 5, 6, 7)

# 关键字可变参数：用**来调用
# 用于在函数体内接收字典，key必须是字符串


def function1(**kwargs):
    print(kwargs)
    pass


# function1({"name": "Kakyoin", "age": 18}) 错误
dictA = {"name": "Kakyoin", "age": 18}
function1(**dictA)  # 正确的一种调用方法
function1(name='peter', age=18)  # 这里是可变的，多少项都可以
function1()


# 混合参数：
def complexFunction(*args, **kwargs):
    '可选参数接收到的是一个元组，关键字参数接收到的是一个字典'
    print(args)
    print(kwargs)
    pass

# 注意，可选参数必须放在关键词参数之前，下面这样是不符合要求的
# def errorComplexFunction(**kwargs, *args):
#     pass


complexFunction(1, 2, 3, 4, name="Kakyoin", age=10)
complexFunction(age=18)
