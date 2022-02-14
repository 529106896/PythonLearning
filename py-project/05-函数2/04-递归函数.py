'''
递归：自己调用自己，必须有一个明确的结束条件
优点：逻辑简单、定义简单
缺点：容易导致栈溢出、内存泄漏
'''


def getFact(n):
    if n == 1:
        return 1
    else:
        return n * getFact(n - 1)


print(getFact(5))


# 用递归来模拟文件结构遍历

import os  # 引入文件操作模块


def findFile(filePath):
    listResult = os.listdir(filePath)  # 得到该路径下所有文件和文件夹
    for item in listResult:
        fullPath = os.path.join(filePath, item)  # 获取完整路径
        if os.path.isdir(fullPath):  # 判断是否是文件夹
            findFile(fullPath)  # 如果是文件夹，再次递归
        else:
            print(item)
            pass
        pass
    return


findFile("E:\\VsCodeTest\\py")
