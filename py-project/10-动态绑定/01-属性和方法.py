'''
动态语言：运行时可以改变结构的语言，比如新的函数、对象、代码
'''

import types


class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass

    def __str__(self) -> str:
        return "name:{}  age:{}".format(self.name, self.age)


xm = Student("xm", 18)
print(xm)
xm.height = "888"  # 动态添加一个height实例属性
print(xm.height)

xh = Student("xh", 19)
# print(xh.height)  xh就没有height属性

Student.height = 999  # 动态添加一个height类属性
xz = Student("xz", 20)
print(xz)
print(xz.height)


# 动态添加实例方法：需要引入types模块
def printInfo(self):
    print("name:{} age:{} height:{}".format(self.name, self.age, self.height))


# 动态绑定方法的语法
xz.printInfo = types.MethodType(printInfo, xz)
xz.printInfo()


# 动态添加类方法，不需要types模块
@classmethod
def printName(cls):
    # print("这是一个类方法，%s" % cls.name)  注意，因为Student的name是实例属性，而类方法不能访问实例属性
    print("这是一个类方法")


Student.printName = printName
xm.printName()

# 静态方法同理，不需要引入types模块
