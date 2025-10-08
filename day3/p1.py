
# Take 5 numbers one after another
num = []
for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    num.append(number)

num.sort()
print("Sorted in ascending order:", num)

num.reverse()
print("Reversed order:", num)