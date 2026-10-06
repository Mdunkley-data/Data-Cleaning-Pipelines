hrs = input("Enter Hours:")
h = float(hrs)
rph = input('Rate Per Hour')
r = float(rph)

if h>40:
    pay=40*r+(h-40)*r*1.5
else:
    pay=h*r
print(pay)