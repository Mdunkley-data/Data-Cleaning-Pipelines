# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
tot=0.0
count=0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    count=count+1
    words=line.split()
    tot=tot+float(words[1])
print('Average spam confidence:',tot/count)