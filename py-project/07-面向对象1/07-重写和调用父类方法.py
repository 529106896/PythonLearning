class Dog:
    name = ""
    color = ""

    def bark(self):
        print("小狗叫")

    def __init__(self, name, color) -> None:  # 如果父类有构造函数，则子类也必须有构造函数
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return "%s %s" % (self.name, self.color)


class Keji(Dog):
    def bark(self):
        print("柯基叫")
        pass

    def __init__(self, name, color) -> None:
        super().__init__(name, color)  # 先调用父类的方法，让Keji可以使用name和color两个属性
        # 如果是多继承，会逐个地调用
        self.name = "柯基"
        self.color = "黑色"

    def __str__(self) -> str:
        return super().__str__()

    pass


keji = Keji("keji", "red")
keji.bark()  # 重写父类方法，会覆盖掉父类的方法
print(keji)
