import urllib
import xml.etree.ElementTree as ET

xmlstring = urllib.urlopen('http://python-data.dr-chuck.net/comments_311923.xml').read()

tree = ET.fromstring(xmlstring)

counts = tree.findall('.//count')

sum = 0
for count in counts:
  sum += int(count.text)

print(sum)
