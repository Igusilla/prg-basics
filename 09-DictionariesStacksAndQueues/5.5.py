paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
unique = set(words)
dictionary = {}
for word in unique:
    dictionary[word]=words.count(word)

print(dictionary)