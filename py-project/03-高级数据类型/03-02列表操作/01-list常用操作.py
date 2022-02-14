'''
append：在列表后面追加元素
count：统计元素出现的次数
extend：扩展，相当于批量添加
index：获取指定元素下标
insert：在指定位置插入
pop：删除最后一个元素
remove：移除左边找到的第一个元素
reverse：反转列表
sort：列表排序
'''
li = [1, 2, 'China']
print(type(li))
print(len(li))  # len 查看序列的长度
print(len("我喜欢China"))

list1 = [1, 2, 3.14, 'China', True]
print(list1)
print(list1[2])
print(list1[0:4:2])
print(list1[::-1])
print(list1 * 2)

list2 = [1, 2, 3, 4]
print(list2)
list2.append(["China", "China"])
print(list2)
list2.insert(1, "China")  # 在指定下标之前插入元素
print(list2)

data = list(range(0, 10))  # 可以先用range生成，然后转换为list对象
print(data)

list2.extend(data)
print(list2)

list3 = list(range(0, 10))
print(list3)
del list3[2:5]  # 从列表中删除元素
print(list3)
list3.remove(8)  # 从列表中删除指定元素
print(list3)
list3.pop(2)  # 从列表中删除指定索引上的元素
print(list3)
print(list3.index(6))  # 从列表中查找元素
print(list3.index(6, 1, 4))  # 在列表的第2个到第5个元素中查找指定元素

list4 = list(range(5))
print(list4)
list4.reverse()
print(list4)

# list5 = [2, 5, 72, "wad", 3, 5, 21, 687, 213, 78, 12, 8, 1]
list5 = [2, 5, 72, 9, 3, 5, 21, 687, 213, 78, 12, 8, 1]
list5.sort()  # 只有相同类型的list才能进行sort
print(list5)
print(list5.count(5))
