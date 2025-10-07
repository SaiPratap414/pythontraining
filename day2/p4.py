text = input("Enter a string: ")

print(text.upper())
print(text.lower())
print(text.title())

# Count characters excluding spaces
count = len(text.replace(' ', ''))
print(f"Character count (excluding spaces): {count}")
