text = "X-DSPAM-Confidence:0.8475"
zpos = text.find('0')
fivepos=text.find('5',zpos)
code=text[zpos:fivepos+1]
c=float(code)
print (c)