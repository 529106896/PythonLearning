# self和对象指向同一个内存地址，可以认为self就是对象的引用
class Person(object):
    age = 0
    name = ""
    gender = ""

    def getSelf(self):
        print(id(self))


class Person1(object):
    age = 0
    name = ""
    gender = ""

    def getSelf(self):
        print(id(self))

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        pass


person1 = Person()
print(id(person1))
person1.getSelf()
# 上面两个打印出来的是一样的

person11 = Person1("Kakyoin", 16, "Male")  # 不需要传递self
print(person11.name)
