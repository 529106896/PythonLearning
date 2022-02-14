# 变量如何定义和使用
# 定义规则：变量名 = 数据
# 变量就是用来存储数据的，和类型无关
# py的数据类型有：数字（int、float、complex、bool）、字符串str、字典dict、元组tuple、列表list
a = 10
# 可以使用type来知道当前变量是什么数据类型
print(type(a))
a = 20
a = 30
a = 'nmsl'
print(type(a))
a = True
print(type(a))
a = 13.6
print(type(a))
# print(a)  # 注意行内注释至少要与代码有两个空格，注释内容和注释符号之间要有一个空格

# 下面简单演示高级数据类型——元组、字典、列表
b = ()  # 元组是小括号
print(type(b))

c = []  # 列表是中括号
print(type(c))

d = {}  # 字典是大括号
print(type(d))

# 下面介绍变量的命名规则
# 变量必须以字母或下划线开头（注意不能以数字开头！），其余部分可以是数字、字母、下划线
# 变量区分大小写
# 不能使用python关键字
_age = 18
print(_age)
