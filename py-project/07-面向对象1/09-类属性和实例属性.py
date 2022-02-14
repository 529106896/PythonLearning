class Person:
    name = "Kakyoin"

    def __init__(self, age) -> None:
        self.age = age
        pass

    pass


person1 = Person(18)
print(person1.name)  # 通过实例对象访问类属性
print(person1.age)  # 通过实例对象访问实例属性

print(Person.name)  # 通过类对象访问类属性
# print(Person.age)  不可用过类对象访问实例属性，只有实例对象才能访问实例属性

person2 = Person(28)
print(person2.name)
print(person2.age)

# 注意，实例属性是每个实例各一份，而类属性是所有实例共一份

person2.name = "Joseph"
print(person1.name)
print(person2.name)

Person.name = "Jotaro"
print(person1.name)
print(person2.name)

# 注意这里，要修改类属性，只能通过类对象去修改
# person2.name 是自己又创建了一个实例属性name，然后修改了name
# person1仍然使用类属性
# 最后的打印中，person1的name仍然是类属性，而person2的name已经变成了实例属性
