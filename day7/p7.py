#abstraction
from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
    def details(self):
        print("details of employee")

class manager(employee):
    def salary(self):  
        return 50000
        
    def team(self):
        print("display team members")

class staff(employee):
    def salary(self):  
        return 30000


m = manager()
m.team()
print(m.salary())

s = staff()
print(s.salary())