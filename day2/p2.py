

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

print("Vowels in the string are:")

for ch in text:
    if ch in vowels:
        count = count +1
print(count)
