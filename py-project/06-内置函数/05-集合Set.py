# set也是一种数据类型，是一个无序且不重复的元素集合
# 不支持索引和切片
'''
集合的操作函数
add
clear
difference 差集
intersection 交集
union 并集
pop
discard
update
'''

# 创建集合的方法：大括号
# 方法一：
set1 = {1, 2, 3}
print(type(set1))

# 方法二：
set2 = set([1, 3, 4, 6])
print(type(set2))

# add 添加
set1.add(4)
print(set1)

# pop 删除第一个元素
tmp = set1.pop()
print(set1)
print(tmp)

# remove 删除指定元素
set1.remove(3)
print(set1)

print('---------')

# discard 删除指定元素
set1.add(5)
print(set1)
set1.discard(5)
print(set1)

print('---------')

# 取差集
print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)
print(set2 - set1)

# 取并集
print(set1.union(set2))

# 取交集
print(set1.intersection(set2))

# update 类似于并集
print(set1)
print(set2)
set1.update(set2)
print(set1)
