def add(a,b=0):
    return a+b
result = add(2,5)
print(result)

def add(a,b,c):
    return a+b+c
result =add(2,5,3)#positinal argument
print(result)

def add(c,b,a):
    return a 
result =add(2,a=5,b=3) #keyword argument
print(result)