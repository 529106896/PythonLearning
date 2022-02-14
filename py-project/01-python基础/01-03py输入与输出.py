# 输出
# 可以使用%来实现占位
name = 'Kakyoin'
age = 18
print('我的名字叫%s，今年%d岁' % (name, age))
# \n可以作为换行符
print('Hello\nWorld!')

# 也可以使用格式化输出，只需要写上大括号，然后format里填上就行
print('姓名：{}，年龄：{}'.format(name, age))

# 输入
# 使用input接收输入，但注意input接收的键盘输入都是str类型，如果需要其他类型需要转换
userName = input("请输入您的姓名：")
# 使用int进行类型转换
userAge = int(input("请输入您的年龄："))
print(type(userName))
print(type(userAge))
print("用户名：%s  用户年龄：%d" % (userName, userAge))
