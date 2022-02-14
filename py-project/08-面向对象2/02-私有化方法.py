# 语法，在方法名前加上两个下划线
# 主要是为了防止子类意外重写
class Animal():
    def eat(self):
        print("吃东西")
        pass

    def __drink(self):
        print("喝东西")


class Dog(Animal):
    pass


d1 = Dog()
d1.eat()
# d1.__drink()  报错，因为__drink是私有方法
