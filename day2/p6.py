
sent = input("Enter a sentence: ")


words = sent.split()


word_count = len(words)


print("Number of words:", word_count)
print("First word:", words[0].title())
print("Last word:", words[-1].title())
print(sent.title())
