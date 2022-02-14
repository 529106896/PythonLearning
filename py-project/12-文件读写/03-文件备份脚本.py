def copyFile():
    # 接收用户输入的文件名
    oldFileName = input("请输入要备份的文件名：")
    # 分割文件名和文件后缀
    fileList = oldFileName.split(".")
    # 构造新的文件名，并加上备份的后缀
    newFileName = fileList[0] + "Backup." + fileList[1]
    oldFile = open('./12-文件读写/' + oldFileName, 'r', encoding='utf-8')
    newFile = open('./12-文件读写/' + newFileName, 'w', encoding='utf-8')
    # 读取旧文件内容
    content = oldFile.read()
    newFile.write(content)
    # 关闭文件
    oldFile.close()
    newFile.close()
    pass


# copyFile()
# 注意，copyFile不适合读取大文件的情况，因为他会把全部内容一次性全部读取然后存到内存中
# 可以改造为一次读取一块


def copyGreatFile():
    # 接收用户输入的文件名
    oldFileName = input("请输入要备份的文件名：")
    # 分割文件名和文件后缀
    fileList = oldFileName.split(".")
    # 构造新的文件名，并加上备份的后缀
    newFileName = fileList[0] + "Backup." + fileList[1]

    try:
        with open('./12-文件读写/' + oldFileName, "r", encoding="utf-8") as oldFile, open(
                './12-文件读写/' + newFileName, "w", encoding="utf-8") as newFile:
            while True:
                content = oldFile.read(1024)  # 一次读取1024字符
                newFile.write(content)
                if len(content) < 1024:  # 如果读取到的小于1024，说明已经读取完了，退出循环
                    break
    except Exception as e:
        print(e)
    pass


copyGreatFile()
