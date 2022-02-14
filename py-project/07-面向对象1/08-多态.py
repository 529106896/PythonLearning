# 多态，即同一行为，对不同子类有不同行为表现
# 多态的两个前提条件：继承 + 重写
class Animal:
    def say(self):
        print("我是一个动物")


class Dog(Animal):
    def say(self):
        print("我是狗")


class Cat(Animal):
    def say(self):
        print("我是猫")


dog1 = Dog()
dog2 = Dog()
cat1 = Cat()
cat2 = Cat()

animalArr = [dog1, dog2, cat1, cat2]

for i in animalArr:
    i.say()
