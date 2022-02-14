'''
函数定义：
def 函数名(参数):
    代码块
    pass
函数内容的第一行可以用字符串进行函数说明
'''


def printRectangle():
    '''
    这个函数用于打印一个三角形
    '''
    for i in range(5):
        j = 5
        while j > i:
            print("*", end=" ")
            j -= 1
        print()


printRectangle()
printRectangle()
printRectangle()
