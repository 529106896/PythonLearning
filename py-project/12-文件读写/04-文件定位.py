# tell 用于获取文件光标当前的位置
file = open("./12-文件读写/test1.txt", 'r', encoding='utf-8')
print(file.read(3))
print(file.tell())
print(file.read(3))
print(file.tell())  # 注意汉字的字符数，此处一个汉字 = 3个字符
file.close()
print("-"*10)

# truncate 对源文件进行截取操作
file = open("./12-文件读写/test1.txt", 'r', encoding='utf-8')
print(file.read())
file.close()
file = open("./12-文件读写/test1.txt", 'r+', encoding='utf-8')
file.truncate(18)  # 因为是截取操作，会修改源文件，所以要以r+的方式打开
print(file.read())
file.close()
print("-"*10)

# seek 指定文件指针位置
# seek(offset, from)
# offset：偏移量，正数向后，负数向前
# from：0从文件开头，1从当前位置，2从文件末尾

file = open("./12-文件读写/test1Backup.txt", 'r', encoding='utf-8')
print(file.read(18))
file.seek(0, 0)
print(file.read(6))
# file.seek(6, 1)  注意，如果没有以b模式打开文件，就只允许从头开始计算文件相对位置
file.seek(6, 0)
print(file.read())
