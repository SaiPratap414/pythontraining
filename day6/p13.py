age="Hello"
if not type(age) is int:
    raise Exception("Age must be an integer")

import random
r = random.Random()
print(r.randint(1, 100))