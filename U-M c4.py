import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Mahdiya.html'

for i in range(7):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup('a')

    chosen_link = links[17]
    name = chosen_link.text
    url = chosen_link.get('href')

print('Last name:', name)
print('Final URL:', url)
