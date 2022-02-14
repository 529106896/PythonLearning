'''
常用操作有：
首字母变大写 capitalize
是否以x结束：endswith
是否以x开始：startswith
检测x是否在字符串中：find
判断是否是字母或数字：isalnum
判断是否是字母：isalpha
判断是否是数字：isdigit
判断是否是小写字母：islower
用指定字符把序列内的元素连接：join
大小写转换：lower/upper
大小写互换：swapcase
移除左右空格：strip lstrip rstrip
切割字符串：split
把每个单词的首字母变大写：title
替换：replace(old, new, count)
统计出现次数：count
'''
name = 'peter'
print('姓名首字母大写：%s' % name.capitalize())
name1 = '   pet er      '
print('去掉首尾空格：%s' % name1.strip(), end="|\n")
print('去掉左边空格：%s' % name1.lstrip(), end="|\n")
print('去掉右边空格：%s' % name1.rstrip(), end="|\n")

# 复制字符串错误演示
name1 = name  # 不能直接用赋值，因为这样其实是把name的内存地址赋值给了b的
print(id(name))  # id()可以用来查看变量的内存地址
print(id(name1))

str1 = 'I love China China'
print(str1.find("China"))  # 返回值是第一次出现的下标
print(str1.find("America"))  # 没找到返回-1
print(str1.index('China'))  # index的功能是检测字符串中是否包含子字符串，返回的是下标
# print(str1.index("America"))  找不到会报错，具体以后再介绍

print("China".lower())
print("China".upper())
print("Make China Great Again!".swapcase())

print("China China China".replace("China", "USA", 2))
print("-".join(["America", "Russia", "China"]))
print("China China China".count("i"))
print("a2".isalnum())
print("china china china".title())
for item in "China China China".split(" "):
    print(item)

strMsg = 'Hello World'
# 切片：slice(start:end:step)
print(strMsg[2:7])  # 这个区间也是左闭右开
print(strMsg[2:])  # 直接取到最后
print(strMsg[:7])  # 从头取到第7个
print(strMsg[::-1])  # 步长为-1直接倒序输出
print("China" * 2)
