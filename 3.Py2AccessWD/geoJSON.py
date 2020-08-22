import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: address = 'University of Delaware'

parms = dict()
parms['address'] = address
parms['key'] = api_key

url = serviceUrl + urllib.parse.urlencode(parms)
print('Retriving', url)
urlHandler = urllib.request.urlopen(url, context=ctx)

data = urlHandler.read().decode()
print('Retrieved', len(data), 'characters')
# print(data)
info = json.loads(data)
print(json.dumps(info, indent=4))

print(info['results'][0]['place_id'])