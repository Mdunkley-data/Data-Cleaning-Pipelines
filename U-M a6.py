ef computepay(h, r):
   if h>40:
     d  pay = 40*r+(h-40)*r*1.5
   else:
       pay = h*r
   return pay

hrs = input("Enter Hours:")
rph = input("Rate Per Hour")
h =float(hrs)
r =float(rph)

p = computepay(h,r)
print("Pay", p)