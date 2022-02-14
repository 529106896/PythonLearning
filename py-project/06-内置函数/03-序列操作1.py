'''
序列操作：
all
any
sorted
reverse
range
zip
enumerate
'''

# all() 判断给定的迭代参数中所有元素是否为True，是则返回True
# 除0、空、False，都算True
# 如

print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))  # 注意，空列表、空元组的返回值是True
print(all(()))

# any 判断给定的迭代参数中所有元素是否为False，是则返回False
# 有一个为True，则返回True
print(any([1, 2, 3]))
print(any([1, 2, 3, 4, 0]))
print(any([0, False, False, 0]))
print(any([]))  # 注意，空列表、空元组的返回值是False
print(any(()))

# 可简单理解为，all是 and ，any是 or
'''
sort和sorted
sort是应用在list上的方法，sorted可以对可迭代的对象进行排序操作
sort是对已经存在的list进行排序，sorted是返回一个新的list

语法：sorted([迭代对象, key, 升序或降序])
'''

list1 = [1, 23, 34, 3546, 5, 6, 345, 32, 4]
list1.sort()  # list自带的sort方法，直接修改的是原始对象
# 注意，这种方法不能用于tuple
print(list1)

list2 = [12, 3, 124, 235, 34, 63, 45, 12, 431, 5, 47645, 6]
print("排序之前{}".format(list2))
sorted(list2)
print("排序之后{}".format(list2))  # 注意，sorted是返回一个新的对象，不是修改原始对象

print("排序之后{}".format(sorted(list2)))
print("降序排序之后{}".format(sorted(list2, reverse=True)))

tuple1 = tuple(list2)
print("元组排序之前{}".format(tuple1))
print("元组排序之后{}".format(sorted(tuple1)))

# 使用key指定排序规则
list3 = [123, 12, 4, 1235, 3426, 5, 762, 13, 12, 412352]
print(sorted(list3, key=lambda x: x * (-1)))  # 按照数字倒数排序

dictArr = [{
    "name": "Kakyoin",
    "age": 17
}, {
    "name": "Joseph",
    "age": 60
}, {
    "name": "Jotaro",
    "age": 17
}, {
    "name": "Fuckyou",
    "age": 60
}]

# 先按照age倒序排序，age相同则按照name排序
print(sorted(dictArr, key=lambda x: (-x["age"], x["name"])))

# reverse 反转列表
list4 = [21, 4, 235, 2356, 34, 3, 2, 42, 5, 2346, 23, 412]
list4.reverse()
print(list4)

# range函数
for i in range(10):
    print(i, end=" ")
print()

# zip函数：用来打包的
s1 = ['a', 'b', 'c']
s2 = ['you', 'me', 'he']
print(list(zip(s1, s2)))
s2.append("Fuck")
print(list(zip(s1, s2)))
s2.pop()
s1.append("Fuck")
print("s1={}\ns2={}".format(s1, s2))
print(list(zip(s1, s2)))  # 元素数量不一样，则按照少的那个来压缩


def printBookInfo():
    books = []
    name = input("请输入书名（以空格分隔）：")
    author = input("请输入作者（以空格分隔）：")
    nameList = name.split(" ")
    authoList = author.split(" ")
    bookInfo = list(zip(nameList, authoList))

    for item in bookInfo:
        tmpInfo = {
            "编号": bookInfo.index(item) + 1,
            "书名": item[0],
            "作者": item[1]
        }
        books.append(tmpInfo)
    for item in books:
        print(item)


printBookInfo()
