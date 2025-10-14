class employee:
    def greet(self):
        print("Hello people")
class manager(employee):
    def greet(self):
        print("Good Morning")
        
class staff(employee):
    def welcome(self):
        print("welcome")
m=manager()
m.greet()

s=staff()
s.greet()