file = open('./12-文件读写/test1.txt', 'r', encoding='utf-8')
print(file.read())  # read默认是读取所有数据
print("-"*10)  # 注意，此时文件指针的位置已经改变
file.close()

file = open('./12-文件读写/test1.txt', 'r', encoding='utf-8')
print(file.read(6))  # 可以指定读取字符的个数
print(file.read())  # 第二次接着上次的读
file.close()
print("-"*10)

file = open('./12-文件读写/test1.txt', 'r', encoding='utf-8')
print(file.readline())  # 一行一行地读
print(file.readline())
file.close()
print("-"*10)

file = open('./12-文件读写/test1.txt', 'r', encoding='utf-8')
print(file.readlines())  # 一次性读取所有行，把内容以列表返回，可以有参数
file.close()
print("-"*10)

# 以二进制方式读，默认是rb
file = open('./12-文件读写/test1.txt', 'rb')
data = file.read()
print(data.decode('utf-8'))  # 先读取，再解码
file.close()
print("-"*10)

'''
with 上下文管理，防止文件句柄发生异常
不管在处理文件过程中是否发生异常，都能保证with语句的执行完毕后关闭已经打开的文件句柄
'''
# with的使用，读写之后不再需要手动close
with open('./12-文件读写/test1.txt', 'r', encoding='utf-8') as f:
    print(f.read())
