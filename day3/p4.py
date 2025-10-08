list1 = []
list2 = []
for i in range(5):
    value = int(input("Enter the number: "))
    if value % 2 == 0:
        list1.append(value)
    else:
        list2.append(value)
print("Even numbers:", list1)
print("Odd numbers:", list2)
