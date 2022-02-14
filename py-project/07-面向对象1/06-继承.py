class Person:
    def eat(self):
        print("吃饭")


class PersonWalk(Person):
    def walk(self):
        print("走路")


class PersonTalk(Person):
    def walk(self):
        print("说话")


person1 = PersonTalk()
person1.eat()
person1.walk()


# 多继承
# class PersonNormal(Person, PersonTalk, PersonWalk):  注意，这种继承是错的，因为PersonTalk和PersonWalk已经继承了Person
class PersonNormal(PersonWalk, PersonTalk):
    def learn(self):
        print("学习")


person2 = PersonNormal()
person2.learn()


# 如果多个父类有相同方法，执行顺序如下：
class D(object):
    def eat(self):
        print("D eat")


class C(D):
    def eat(self):
        print("C eat")


class B(D):
    pass


class A(B, C):
    pass


a = A()
a.eat()
'''
在执行a.eat时，先去A中查找，A中没有，去A的第一个父类B中查找；如果B中没有，则去第二个父类C中查找（注意，并没有去B的父类中取查找）
即 广度优先 BFS
顺序：A——B——C——D，也是继承的顺序

同时，C也是重写了D的eat方法
'''
# 使用一个魔术方法来验证，mro用来显示继承关系
print(A.__mro__)
