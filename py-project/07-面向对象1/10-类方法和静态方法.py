'''
类方法需要以@classmethod修饰，所有权归类对象所有
类方法主要用于对类属性进行访问和修改
需要cls作为参数

静态方法需要用@staticmethod修饰，不任何强制参数
静态方法主要用来存放逻辑性的代码，本身和类、实例对象没什么交互，不怎么会涉及到类中的方法和属性操作
好处在于数据资源可以得到有效利用，不需要实例化
'''


class Person():
    county = "China"

    def getCountry(self):  # 这个方法是一个实例方法
        return self.county
        pass

    @classmethod
    def getCountry1(cls):  # 必须有一个cls参数
        return cls.county

    @classmethod
    def changeCountry(cls, data):
        cls.county = data

    @staticmethod
    def getData():  # 可以不传参数
        return Person.county  # 需要用这种方法来访问属性

    pass


person1 = Person()
print(Person.getCountry1())
# print(Person.getCountry())  这个会报错，因为这是个实例方法

print(person1.getCountry())
print(person1.getCountry1())  # 实例对象可以访问类方法

Person.changeCountry("中国")
print(Person.getCountry1())
print(person1.getCountry())
print(person1.getCountry1())

person1.changeCountry("china")
print(Person.getCountry1())
print(person1.getCountry())
print(person1.getCountry1())

print(Person.getData())  # 类对象可以访问静态方法
print(person1.getData())  # 实例对象可以访问静态方法，但一般不会这样用

import time


class TimeTest:
    # 比如这个方法，只是用于显示当前时间，就不需要去实例化，可以做成一个静态方法
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())

    # def __init__(self, hour, min, sec) -> None:
    #     self.hour = hour
    #     self.min = min
    #     self.sec = sec


print(TimeTest.showTime())
'''
类方法的第一个参数是cls，通过cls引用类的属性和方法
实例方法的第一个参数是self，self可以引用类属性和实例属性，如果类属性和实例属性同名，优先使用实例属性
静态方法不需要额外参数，如果在静态方法中要使用类属性，需要用类对象来引用

类对象可以使用类的属性和方法，不可以使用实例属性和实例方法
实例对象则都可以
'''
