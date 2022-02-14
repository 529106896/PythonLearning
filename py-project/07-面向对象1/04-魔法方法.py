'''
常用的魔法方法：
init  类似构造函数
str  类似toString
new  创建并返回一个实例对象
class  获取对象的类
del  释放资源，类似于delete
'''


class Person:
    name = ""
    age = 0
    gender = ""

    def __init__(self, name, age, gender) -> None:
        print("running init function")
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:  # 注意要有返回值
        return "%s %d %s" % (self.name, self.age, self.gender)

    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法，每调用一次都会生成一个新的对象

        可以用于控制对象的一些属性，经常用于单例模式
        '''
        print("running new function")
        # 此处必须有一个return
        return object.__new__(cls)  # 会首先执行new函数，然后执行init函数，此处真正创建对象实例


person1 = Person("Kakyoin", 18, "Male")
print(person1)  # 没有重写的str会返回内存地址
print(person1.__class__)

'''
init 和 new
new：类的实例化方法，必须返回一个实例，否则对象创建不成功
init：用来做属性的初始化工作，相当于实例的构造方法

new：必须有一个cls参数，代表要实例化的类
'''
