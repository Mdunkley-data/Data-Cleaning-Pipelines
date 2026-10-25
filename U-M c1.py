import re
hand=open('regex_sum_2480711.txt')
total=0

for line in hand:
    numbers= re.findall('^[0-9]+',line)
    for number in numbers:
        total=total+int(number)
        
print(total)
