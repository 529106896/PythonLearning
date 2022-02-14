# 局部变量
# 局部变量就是在函数内部定义的变量，作用域仅仅局限于函数的内部

# 全局变量
profession = 'Software Engineering'


def function1():
    '''
    注意这里，当全局变量和局部变量相同时，函数会优先使用局部变量
    '''
    profession = 'Internet Safety'
    print(profession)


def changeGlobal():
    '如果在函数内部要修改全局变量，使用关键字global先进行声明'
    global profession
    profession = 'Computer Science'


def function2():
    print(profession)


changeGlobal()
print(profession)
function1()
function2()
