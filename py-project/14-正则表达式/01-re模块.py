# 使用re模块来快速使用正则表达式
# re.match(pattern, string, flags=0)
# pattern 正则表达式
# string 要匹配的字符串
# flags 标志位，控制匹配方式
import re

myString = "Python is the best language in the World"
result = re.match("P", myString)
# result = re.match("y", myString)  这样会匹配不到
# result = re.match("Python", myString)  这样可以匹配到
# match 只能匹配以xxx开头的，且匹配一次之后就返回
print(type(result))
print(result.group())  # 用group获取匹配结果
# 如果有多个匹配结果，会以元组的形式存放到group中

'''
flag可选标志位：（可使用 | 选择多个标志位）
re.I 大小写不敏感
re.L 本地化识别
re.M 多行匹配
re.S 使用.匹配包括换行在内所有字符
re.U 使用Unicode匹配
re.X 更灵活的正则表达式
'''
result = re.match("python", myString, re.I)
print(result)
print(result.group())

result = re.match("(.*) is (.*?) .*", myString, re.I)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(0))
# print(result.group(3)) 此行会报错，因为匹配的只是Python is the
print(result.groups())  # 以元组的形式返回结果，用参数没用
print(result.groups()[1])
