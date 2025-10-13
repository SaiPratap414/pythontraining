from datetime import datetime
dt = datetime.now()
print(dt)
t = dt.timestamp()
print(t)

d = datetime.fromtimestamp(t)
print(d)