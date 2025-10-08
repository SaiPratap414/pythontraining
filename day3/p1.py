
num = input("Enter five numbers: ").split()
num = [int(x) for x in num]

num.sort()
print("Sorted in ascending order:", num)

num.reverse()
print("Reversed order:", num)