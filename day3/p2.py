list1 = [2,3,4,5,6]
list2 = [9,8,1,7,3]

list3 = list1.copy()  
list3.extend(list2)
print("Merged list:", list3)

list3.sort()
print("Sorted merged list:", list3)