import requests

token = #Token Goes Here
r = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

print r.status_code
print r.headers
print r.content
