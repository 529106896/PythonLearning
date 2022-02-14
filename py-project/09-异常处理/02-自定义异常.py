'''
自定义异常，直接或间接继承Error或Exception类
使用raise捕获
'''


import traceback


class demoException(Exception):
    def __init__(self, len):
        self.len = len
        pass

    def __str__(self):
        return "输入长度是 " + str(self.len) + " ，不符合规定"

    pass


def nameInput():
    name = input("请输入姓名：")
    try:
        if len(name) > 4 or len(name) <= 0:
            raise demoException(len(name))
    except demoException as e:
        print(e)
        traceback.print_exc()
        pass
    else:
        print(name)


nameInput()
