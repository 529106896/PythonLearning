'''
__slots__：用来限制可以添加的属性，防止出现乱添加的情况
__slots__不会被子类继承，只在当前类内有效
'''


class Student():
    __slots__ = ("name", "age")  # 后面的是字符串

    def __str__(self) -> str:
        return "name:{} age:{}".format(self.name, self.age)


xm = Student()
xm.name = "Kakyoin"
xm.age = 17
print(xm)
# print(xm.__dict__)  # 用于查看所有可用的属性，只有在没有slots时才能使用
# xm.score = 99  # 不在slots范围内的属性会添加失败


class SubStudent(Student):
    __slots__ = ("gender")  # 当子类声明了slots属性是，才会继承父类的slots，子类的slots范围 = 父类slots + 自己的slots


xz = SubStudent()
xz.name = "Joseph"
xz.age = 60
print(xz)
xz.gender = "Male"
