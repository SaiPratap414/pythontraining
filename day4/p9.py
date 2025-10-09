# x=10
# def f1():
#     print(x)
# def f2():
#     print(x)
# print(x)
# f1()
# f2()

x=5
def f1():
    x=10
    print(x)
    def f2():
        x=20
        print(x)
    f2()
print(x)
f1()

def f3():
    global y
    y=10
f3()
y=y+5
print(y)