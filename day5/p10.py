def f2(f):
    def wrapper(role):
        if role == "VP":
            print("Bonus is 20 percent")
        else:
            print("Bonus is 10 percent")
        return f(role)
    return wrapper
@f2       
def f1(role):
    print(f"Hello{role}")
f1("VP")