para = input("Enter a para: ")

old = input("Enter the word to replace: ")
replaced = input("Enter the replacement word: ")

count = para.count(old)

new_para = para.replace(old, replaced)

print("New paragraph:")
print(new_para)

print(f"Number of replacements made: {count}")