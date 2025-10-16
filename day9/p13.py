from collections import deque
d = deque([4,5,3,2])
d.append(0)
print(d)
d.appendleft(9)
print(d)
d.extend([1,2,3])
print(d)
d.extendleft([7,8,9])
print(d)
d.pop()
print(d)
d.popleft() # removes from left
print(d)
d.rotate(2) # rotates right
print(d)