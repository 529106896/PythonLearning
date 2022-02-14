# 语法：
# 两个下划线开头，声明该属性为私有，不能再类的外部被使用或直接访问
# class Person:
#   __age = 18

# protected属性和方法是一个下划线开头


class Person:
    __age = 18  # 私有化类属性

    def __init__(self) -> None:
        self.__name = "Kakyoin"  # 私有化实例属性

    def __str__(self) -> str:
        return "name：%s  age：%d" % (self.__name, self.__age)

    # 使用set get方法访问和修改私有属性
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


class Male(Person):
    def printInfo(self):
        print(self.__name)  # 子类不能继承父类的私有属性

    pass


person1 = Person()
# print(person1.__age)  # 此处会报错：没有这个属性
# print(person1.__name)  # 此处会报错：没有这个属性
print(person1.__str__())  # 类的方法可以访问内部数据
print(person1)
male1 = Male()
# male1.printInfo()

print(male1.getName())
male1.setAge(19)
print(male1.getAge())
# print(Male.getAge())
