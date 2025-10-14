class employee:
    def greet(self, name=None, age=None):
        
        if name and age:
            print(f"Hello {name}, you are {age} years old.")
        elif name:
            print(f"Hello {name}")
        else:
            print("Hello")
e = employee()
e.greet()
e.greet("pratap")
e.greet("pratap", 23)