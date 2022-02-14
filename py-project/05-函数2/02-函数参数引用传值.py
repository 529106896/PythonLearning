'''
在py中，万物都是对象，变量都是对象的引用
'''
a = 1


def func(x):
    print('x的地址是：%s' % str(id(x)))
    pass


def func1(x):
    print('x修改前的地址是：%s' % str(id(x)))
    x = 2
    print('x修改后的地址是：{}'.format(id(x)))
    pass


print('a的地址是：%s' % str(id(a)))
func(a)
# 这里会发现，两个打印的内存地址都是一样的，说明他们是对同一个对象的引用

print('a的地址是：%s' % str(id(a)))
func1(a)
# 这里会发现，x修改前后的地址不一样
print(a)
# 输出a，发现a并没有被改变，因为int、str、tuple都是不可变类型，每次修改都是开辟一个新的内存空间，然后指向新的内存空间
# func1传的的只是a的内存空间的一个引用，并没有改变内存空间里的东西，而是开辟了一个新的

# 可变类型举例：list和dict
li = [9, 9, 9]


def changeList(tmp):
    print("tmp改变前的内存地址：{}".format(id(tmp)))
    print("tmp改变前：{}".format(tmp))
    tmp.append([1, 2, 3, 4])
    print("tmp改变后的内存地址：{}".format(id(tmp)))
    print("tmp改变后：{}".format(tmp))
    pass


print("li改变前的内存地址：{}".format(id(li)))
print("li改变前：{}".format(li))
changeList(li)
print('li改变后：{}'.format(li))
# 输出之后，可以发现li和tmp都是一样的


'''
总结：
1. 在python中，万物皆对象，在函数调用时，实参传递的就是对象的引用
2. 要知道函数内部的处理是否会影响外部数据的变化
'''
