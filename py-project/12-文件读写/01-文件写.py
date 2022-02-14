'''
文件操作一般步骤：
打开文件、读写文件、保存文件、关闭文件
'''
# 打开文件：open(路径, 打开模式)
# 常用模式：
# r：默认模式，以只读方式打开，文件指针会放在文件开头
# w：写入，已存在就覆盖，不存在就创建
# a：追加，存在就指针放结尾，不存在就创建

# 打开文件
# 注意，默认打开的编码模式是GBK
# 最好在打开时指定一个编码类型
file = open('./12-文件读写/test.txt', 'w', encoding='utf-8')

# 读写文件
file.write('我爱China')
file.write('\n无产阶级，联合起来！')  # 注意，w模式下打开会覆盖

# 保存并关闭文件
file.close()

# 以二进制方式读写
file = open('./12-文件读写/test1.txt', 'wb')
file.write('叔叔我啊，最喜欢钱了'.encode('utf-8'))  # 注意，用encode是把字符串转换成了bytes
file.close()

# 追加方式（有不覆盖，没有就创建）
file = open('./12-文件读写/test1.txt', 'a', encoding='utf-8')
file.write('\n曹仁，南蛮什么时候杀啊')  # 不是二进制就不需要用encode
file.write('\n你所热爱的，就是你的生活！')
file.close()

# 二进制追加
file = open('./12-文件读写/test1.txt', 'ab')
file.write('\n我们承诺：……'.encode('utf-8'))
file.close()
