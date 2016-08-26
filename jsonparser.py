import json
import urllib

url = raw_input('Enter the url: ')
jsonstring = urllib.urlopen(url).read()

dict = json.loads(jsonstring)

sum = 0
for comment in dict['comments']:
  sum += int(comment['count'])

print(sum)
