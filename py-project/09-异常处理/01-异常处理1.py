'''
语法格式：
try:
    可能出错的代码块
    pass
except:
(指定错误类型：excepte ZeroDivisionError as e:)
    出错后执行的代码块
    pass
else:
    没有出错的代码块
    pass
finally:
    不管是否出错都会执行的代码块
'''

import traceback


try:
    print(b)
    pass
except NameError as e:
    print(e)
else:
    pass

try:
    li = [1, 2]
    print(li[2])
    pass
except IndexError as e:
    print(e)
except NameError as e:  # 可以有多个except
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:  # 所有异常的父类是BaseException
    print(e)
else:
    pass

try:
    a = 10/0
# except ZeroDivisionError as e:
#     print("In ZeroDivisionError")
#     print(e)
except Exception as e:
    print("In Exception")
    print(e)
    traceback.print_exc()  # 可以使用traceback.print_exc()来这哪是更详细的报错信息
else:
    pass
