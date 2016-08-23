import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter the url: ')
socketfile = urllib.urlopen(url)

dataWithHtml = socketfile.read()
soup = BeautifulSoup(dataWithHtml,'html.parser')
anchorTags = soup('a')

for tag in anchorTags:
  print(tag.get('href', None))
