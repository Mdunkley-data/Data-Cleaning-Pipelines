fname = input("Enter file name: ")
fh = open(fname)
unique_words = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)