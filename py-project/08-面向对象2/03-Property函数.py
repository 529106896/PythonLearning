# 让私有属性可以以.的方式去访问，不用调用set、get方法
'''
实现方法1：
    类属性，即在类中定义值为property对象的类属性
'''


class Person():
    def __init__(self) -> None:
        self.__age = 18

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    # 定义一个类属性，就可以直接用访问类的方法修改私有属性
    # property的参数的方法必须以set、get开头
    age = property(getAge, setAge)


person1 = Person()
print(person1.age)
person1.age = 19
print(person1.age)


# 第二种实现方法，在方法上加上装饰器
class Animal():
    def __init__(self) -> None:
        self.__type = "dog"

    @property  # 使用装饰器对type进行装饰，设置为一个getter方法
    def type(self):
        return self.__type

    @type.setter  # 使用装饰器进行装饰，设置为一个setter方法
    def type(self, type):
        self.__type = type


animal1 = Animal()
print(animal1.type)
animal1.type = "cat"
print(animal1.type)
