from collections import namedtuple
price = namedtuple('price', ["Laptop", "Mobile", "Tablet"])
p1 = price(45000, 15000, 25000)
print(p1)
print(p1.Laptop)
print(p1.Mobile)