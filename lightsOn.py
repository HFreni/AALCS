import sys
import requests

#TODO: Add All Stuff to Crontab
#Refactor & Add More Modes
#afplay plays music, music solely intended for personal listening, I own a copy, just made it into wav file.

payload = {"power": "on", "color": "rgb:255,255,255", "brightness": 0.50}

token = sys.argv[1]
mode = sys.argv[2]

r = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

def allon():
    payload = {"power": "on", "color": "rgb:255,255,255",  "brightness": 0.80}
    c = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload,  auth=(token, ''))
    print c.status_code
    print c.headers
    print c.content
    print payload

def rom():
    new = {"power": "on", "color": "rgb:255,0,0", "brightness": 0.50}
    g = requests.put('https://api.lifx.com/v1/lights/all/state', data=new, auth=(token, ''))
    print g.status_code
    print g.headers
    print g.content
    print new


if mode == "allon" :
    allon()
elif mode == "rom" :
    rom()

print r.status_code
print r.headers 
print r.content

