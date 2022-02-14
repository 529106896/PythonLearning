# enumrate 主要用于为序列中的元素加上索引，一般用在for循环中

listObj = ['a', 'b', 'c']
for item in enumerate(listObj):
    print(item)  # 会以元组形式打印出索引和对应的值

for index, item in enumerate(listObj):
    print(index, item)

print("--------------")

for index, item in enumerate(listObj, 1):  # 第二个参数用来指定从哪个下标开始，默认从0开始
    print(index, item)

myDict = {}
myDict["name"] = "Kakyoin"
myDict["age"] = 18
myDict["height"] = 180

# 对于字典，获取到的值是key
for item in enumerate(myDict):
    print(item)
