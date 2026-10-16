fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    # Skip lines that don't start with 'From '
    if not line.startswith('From '):
        continue
    
    # Split the line into words
    words = line.split()
    
    # The email is the second word (index 1)
    print(words[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")



















