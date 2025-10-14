class employee:
    def __init__(self, id):
        self.id = id
        print("Employee Id is ", self.id)

class manager(employee):
    def __init__(self, id, name, city):
        super().__init__(id)  
        self.name = name
        self.city = city

    def details(self):
        print(f"{self.name} is from {self.city}")

m = manager(101, "sai", "bangalore")
m.details()