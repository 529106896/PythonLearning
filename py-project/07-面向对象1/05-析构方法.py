# 析构方法，即__del__()
class Person:
    name = ""

    def __init__(self, name) -> None:
        self.name = name
        print("%s执行构造方法" % self.name)

    def __del__(self):
        print("%s执行析构方法" % self.name)


person1 = Person("Kakyoin")
del person1  # 手动删除、程序执行结束，对象销毁时执行析构函数
person2 = Person("Jotaro")
