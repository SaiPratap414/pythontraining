# # def gen():
# #     for i in range(100):
# #         yield i
# # result = gen()
# # print(list(result))

# # t =(1,2,3,4,5)
# # print(type(t))


# gen1 = (x for x in range(100))
# print(type(gen1)) # print <class 'generator'>

# gen2 =(x for x in range(3))
# print(next(gen2)) # print 0
# print(next(gen2)) # print 1
# print(next(gen2)) # StopIteration

list1 =[1,2,3,4,5,6]
g1 = iter(list1)
print(type(g1)) # print <class 'list_iterator'>
print(type(list1)) # print <class 'list'>

import sys
list1 =[x for x in range(100000)]
g1=(x for x in range(100000))
print(sys.getsizeof(list1, "Bytes"))
print(sys.getsizeof(g1, "Bytes")) 