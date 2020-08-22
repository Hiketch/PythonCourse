import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: address='http://py4e-data.dr-chuck.net/comments_678847.xml'

url = urllib.request.urlopen(address, context=ctx).read()
data = url.decode()
print(f'Retrieved {len(data)} characters')

# print(type(data))
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
sum = 0

for count in counts:
    sum += int(count.find('count').text)  

print(f'Count: {len(counts)}\nSum: {sum}')