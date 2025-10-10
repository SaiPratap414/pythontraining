# def calc(x):
#     return x+2
# result = map(calc,[20,23,28])
# print(list(result))

# def calc(x):
#     return x>20
# list1= [20,23,28]
# list2 = filter(calc,list1)
# print(list(list2))



from functools import reduce
def calc(x,y):
    return x+y
list1= [20,23,28]
list2 = reduce(calc,list1)
print(list2)