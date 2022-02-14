# os模块主要提供系统级别的一些命令
# 常用操作：
# rename 重命名
# remove 删除文件
# mkdir 创建文件夹
# rmdir 删除文件夹
# getcwd 获取当前目录
# chdir 切换路径
# os.path.join 路径拼接
import os
import shutil

print(os.getcwd())
try:
    os.rename("./13-模块/test.txt", "./13-模块/renameTest.txt")
except Exception as e:
    print(e)
    os.rename("./13-模块/renameTest.txt", "./13-模块/test.txt")

try:
    os.remove("./13-模块/testDel.txt")
except Exception as e:
    print(e)
    tmpFile = open("./13-模块/testDel.txt", "w")
    tmpFile.close()

# 创建多级目录：makedirs
try:
    os.makedirs("./13-模块/test/test/test")
except Exception as e:
    print(e)

# 删除目录 rmdir
try:
    os.rmdir("./13-模块/test")  # 注意，只能删除空目录
except Exception as e:
    print(e)
    # 如果要删除非空目录，需要引入shutill
    shutil.rmtree('./13-模块/test')

print(os.path.join(os.getcwd(), "13-模块"))

print("-"*10)

# 获取指明路径下所有文件的列表
for item in os.listdir(os.getcwd()):
    print(item)
print("-"*10)
# 新版本的遍历列表，最好结合with使用，可以自动释放资源
with os.scandir(os.getcwd()) as tmpDir:
    for item in tmpDir:
        print(item.name)
print("-"*10)
for item in os.listdir(os.getcwd()):
    if os.path.isfile(item):
        print(str(item) + " 是文件")
    if os.path.isdir(item):
        print(str(item) + " 是路径")
