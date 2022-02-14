# 简单理解，__init__就是构造函数
class Person:
    age = 0
    name = "Unknown"
    gender = "Unknown"

    # def __init__(self) -> None:
    #     self.age = 18d
    #     self.name = "Kakyoin"
    #     self.gender = "male"
    # 注意，一个类只能有一个构造函数，不能同时有默认构造函数和有参构造函数

    def __init__(self, name, age, gender) -> None:
        '这种带下划线的函数是py的内置特殊函数，又叫做魔术方法'
        self.name = name
        self.age = age
        self.gender = gender

    def showSelf(self):
        print("%s %d %s" % (self.name, self.age, self.gender))


person1 = Person("Kakyoin", 18, "Male")
person1.showSelf()
# person2 = Person()
# person2.showSelf()
