# def f1():
#     print("Hello")  
# def f2(func):
#     func()
# f2(f1)

def f1():
    def func():
        return 5
    return func
f2=f1()
result = f2()
print(result)

