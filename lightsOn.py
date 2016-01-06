import sys
import requests

payload = {"power": "on", "color": "rgb:255,255,255", "brightness": 0.50}

token = sys.argv[1]

r = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))
c = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload,  auth=(token, ''))

print c.status_code
print c.headers
print c.content


print r.status_code
print r.headers
print r.content

