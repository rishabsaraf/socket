import urllib

socketfile = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in socketfile:
  print (line.strip())

