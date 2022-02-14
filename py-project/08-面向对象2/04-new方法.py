'''
__new__方法的作用是，创建并返回一个实例对象，new调用一次就会得到一个新对象
注意事项：
    new是一个对象实例化时调用的第一个方法
    new至少要有一个参数cls，代表要实例化的类。在调用时由解释器自动提供，其他参数用来传给init
    new决定是否要调用init，因为new可以调用其他类的构造方法或者直接返回别的实例对象作为本类的实例
    在new方法中，不能再调用自己的new方法，会爆栈
'''


class Person():
    def __init__(self) -> None:
        self.color = "红色"

    # new一般是这三个参数，如果不重写new方法，默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


# 一般用new方法来实现单例模式
'''
单例模式是一种设计模式，确保整个系统中只有一个实例
简单的说就是不管创建多少次对象，类返回的都是最初创建的对象，而不会再新建其他对象
一般基于new来实现单例模式
'''


class DataBaseClass():
    def __new__(cls, *args, **kwargs):
        # cls._instance = cls.__new__()  不可以这样使用，不能调用自己的new方法
        if not hasattr(cls, '_instance'):  # 如果不存在，就开始创建
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


db1 = DataBaseClass()
print(id(db1))
db2 = DataBaseClass()
print(id(db2))
