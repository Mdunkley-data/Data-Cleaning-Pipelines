import urllib.request
from bs4 import BeautifulSoup

url='http://py4e-data.dr-chuck.net/comments_2480713.html'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('span')
total=0

for tag in tags:
    number=int(tag.text)
    total=total+number

print('Count', len(tags))
print('Sum',total)
        
