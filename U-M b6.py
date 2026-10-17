name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


many=dict()
for line in handle:
    
    if not line.startswith('From '):
        continue
    
    wds=line.split()
    
    email=wds[1]
    many[email]=many.get(email,0)+1
        
#Find the most prolific commmitter
 
bigword=None
bigcount=None
for key, value in many.items():
     if bigcount is None or value>bigcount:
        bigword=key
        bigcount=value
        
print(bigword,bigcount)