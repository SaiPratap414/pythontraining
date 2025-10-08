numbers = []
for i in range(5):
    num = int(input(f"Enter number : "))
    numbers.append(num)
numbers = list(set(numbers))
print(numbers)

list1 =[]
list2 =[]
for i in range(5):
    value = int(input("Enter the number"))
    list1.append(value)
    if value not in list2:
        list2.append(value)
print (list1)
print (list2)
    