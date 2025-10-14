class employee:
    def salary(self):
        print("salary calculation")
        
class manager(employee):  # Inherit from employee
    def team(self):
        print("display team members")
        
m = manager()
m.team()
m.salary()  # Now manager has access to salary()
