# list1 = [1,2,3,4,5]
# list2 =[i for i in range(5) if i<4] #list comprehension
# print(list2) 

# list2=[]
# for i in list1:
#     list2.append(i+2)
# print(list2)

# list2 =[i+2 for i in list1 if i<4]
# print(list2)


# set = {i+2 for i in list1 if i<4}
# print(set)

employees = {f"emp{i+1}": 1001+i for i in range(5)}
print(employees)

