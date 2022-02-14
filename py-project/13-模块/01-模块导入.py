import time

from black import mypyc_attr  # 导入模块
print(time.ctime())  # 调用模块中的函数

'''
遇到import，会先在当前目录下搜索，然后去环境变量中搜索（使用sys.path查看环境变量）
如果还找不到，去默认路径下查询（一般是python的安装路径）
'''
import sys
print(sys.path)

# 如果想只导入模块中的几个函数，使用from
# 只导入time模块中的ctime和time：
# from time import ctime, time
# 之后使用直接ctime()、time()即可，不需要添加前缀
# 使用from，后面导入的会覆盖前面的

from time import ctime
print(ctime())

# 使用as给导入的模块取别名
import time as myTime
print(myTime.time())
