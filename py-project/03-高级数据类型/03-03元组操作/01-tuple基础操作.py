tupleA = (1, )
tupleB = (1)
tupleC = ()
print(type(tupleA))
print(type(tupleB))
print(type(tupleC))

# 元组只能获取和查询，不能修改和删除
tuple1 = tuple(range(10))
print(tuple1)
print(tuple1[2:4])
for item in tuple1:
    print(item, end=" ")
    pass
print()
print(tuple1[::-1])
print(tuple1[::-2])  # 从倒数第一个开始，隔一个取一次
print(tuple1[::-3])

tuple2 = (1, 2, 3, list(range(10, 20)), 'China')
print(tuple2)
tuple2[3][0] = 100
print(tuple2)
# tuple2[4][0] = 'A'
# 只能修改元组中的list对象，其余的都不能修改
print(tuple2.index(2))
print(tuple2.count(3))
