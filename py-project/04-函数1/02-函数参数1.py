def printRectangle(times, rows):
    '''
    这个函数用于打印一个三角形
    '''
    while times > 0:
        for i in range(rows):
            j = rows
            while j > i:
                print("*", end=" ")
                j -= 1
            print()
        times -= 1


printRectangle(1, 4)
printRectangle(1, 6)
