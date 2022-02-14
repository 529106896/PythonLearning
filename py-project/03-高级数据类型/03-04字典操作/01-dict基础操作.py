'''
常用方法：
修改元素
新增元素
删除元素
统计个数

获取键值
获取值
获取键值对
删除指定键
'''
dict1 = {}
print(type(dict1))
dict1['name'] = "Kakyoin"  # 可以直接用这种方式去添加字典里的元素
dict1['age'] = 18
dict1['pro'] = 'Singer'
print(dict1)
print(len(dict1))

dict2 = {'name': "Van", "age": 19}
print(dict2)

print(dict2['name'])  # 根据键值直接获取Value
dict2['name'] = "Jotaro"
print(dict2['name'])

print(list(dict2.keys()))  # 获取字典的所有键
print(dict2.values())  # 获取字典所有值
print(dict2.items())  # 获取字典的所有键值对

# 经常用items()来遍历dict
for item in dict2.items():
    print(item)

for key, value in dict2.items():
    print("{} = {}".format(key, value))
    pass

# 可以用updata来修改字典
dict2.update({'name': 'Joseph'})
dict2.update({'height': 1.95})
print(dict2)

# 删除操作
del dict2['height']
print(dict2)
dict2['height'] = 1.95
print(dict2)
dict2.pop('height')
print(dict2)

# 字典排序
# python内置的排序函数sorted
print(sorted(dict2.items(), key=lambda d: d[0]))  # 按照key排序
# print(sorted(dict2.items(), key=lambda d: d[1]))  # 按照value排序（但是这里会报错，因为str和int不能比较）
dict3 = {}
dict3['name'] = 'Joseph'
dict3['age'] = '19'
print(dict3)
print(sorted(dict3.items(), key=lambda d: d[1]))
