import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter the url: ')
count = int(raw_input('Enter the count: '))
position = int(raw_input('Enter the position: '))

for i in range(count):
  socketfile = urllib.urlopen(url)
  dataWithHtml = socketfile.read()
  soup = BeautifulSoup(dataWithHtml,'html.parser')
  anchorTags = soup('a')
  url = anchorTags[position-1].get('href')
  name = anchorTags[position-1].contents[0]

print(name)

