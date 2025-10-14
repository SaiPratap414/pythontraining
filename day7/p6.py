class employee:
    def __init__(self,name):
        self.name=name
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
e=employee("pratap")
print(e.getname())
e.setname("pooja")
print(e.getname())