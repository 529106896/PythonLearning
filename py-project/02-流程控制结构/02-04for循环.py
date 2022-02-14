'''
for循环语法：
for 临时变量 in 字符串 or 列表等:
    代码
    pass
'''
tag = "我是一个中国人"
for tmp in tag:
    print(tmp)
    pass

# range 此函数可以生成一个数据集合列表
# range(起始，结束，步长)
# 注意，起始和结束是左闭右开，即[起始, 结束)
# 比如从 1 到 30
for data in range(1, 31):  # 注意右区间是开区间
    print(data, end=' ')
    pass
print()

# break和continue和其他语言中的功能一样
for tmp in range(1, 101):
    if tmp <= 50:
        if tmp % 2 == 0:
            continue
        print("%d还没超过一半" % tmp)
    else:
        break
print("超过一半，退出for循环")
