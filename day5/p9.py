def f2(func):
    def wrapper():
        print("Decorator: Before calling function")
        func()
        print("Decorator: After calling function")
    return wrapper

@f2
def f1():
    print("I am f1 driver")
f1()
