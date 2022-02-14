def function1():
    print("func1 start")
    print("func1 running")
    print("func1 end")


def function2():
    print("func2 start")
    function1()
    print("func2 end")


function2()
