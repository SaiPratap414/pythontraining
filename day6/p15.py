class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b

c = calc(5,4)
print("Addition:", c.add())
print("Subtraction:", c.sub())
print("Multiplication:", c.mul())