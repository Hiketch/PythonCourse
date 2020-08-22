import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

adress = input('Enter location: ')
if len(adress) < 1: adress = 'http://py4e-data.dr-chuck.net/comments_678848.json'
url = urllib.request.urlopen(adress, context=ctx)

data = url.read().decode()
print(f'Retrieved {len(data)} characters')

info = json.loads(data)
# print(json.dumps(info, indent=2))
# print(type(info))

totalSum = 0
for item in info['comments']:
    totalSum += (item['count'])

print(f'Count', len(info['comments']))
print(f'Sum {totalSum}')

