# 类Class由三个部分构成：
# 类名、类的属性、类的方法
class Person:
    age = 18
    name = "Kakyoin"
    height = 180  # 方法外面的属性叫做类属性

    def sayName(self):  # 类方法必须包含参数self（也可以不叫self），且为第一个参数
        print(self.name)  # 定义在方法里，使用self引用的属性叫做实例属性

    def eat(self):
        print("我要吃饭")

    def __init__(self) -> None:
        self.name = 'Joseph'


# 创建对象
person1 = Person()
print(person1.age)
print(person1.height)
person1.sayName()
