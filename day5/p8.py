# sqr = lambda x:x+2
# print(sqr(5))


# # def sqr(x):
# #     return x+2

# result = map(sqr,[3,5,6])
# print(list(result))

result = map(lambda x:x+2,[3,5,6])
print(list(result))

result = filter(lambda x:x>2,[3,5,6])
print(list(result))