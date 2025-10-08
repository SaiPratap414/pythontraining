sent = input("Enter a sentence: ")
list = sent.split()
word_count = {}
for word in list:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)