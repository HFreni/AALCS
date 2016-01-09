import sys
import requests
import time

#TODO: Add All Stuff to Crontab
#Refactor & Add More Modes
#afplay plays music, music solely intended for personal listening, I own a copy, just made it into wav file.

#Configs
allOn={"power":"on", "color":"rgb:255,255,255", "brightness":1}
allOff={"power":"off"}
rom={"power":"on", "color":"rgb:255,0,0", "brightness":.50}
codeRed={"power":"on", "color":"rgb:255,0,0", "brightness":1}
rainDay={"power":"on"}
wakeUp={"power":"on"}

#CLI Tokens
token = sys.argv[1]
mode = sys.argv[2]

#ForDebug
auth= requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

def sendReq(payload):
    c = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
    #For Debugging
    print c.status_code
    print c.headers
    print c.content
    print payload

def lightsOn():
    sendReq(allOn)

def romA():
    sendReq(rom)

def cr():
    while True:
        sendReq(codeRed)
        time.sleep(10)
        sendReq(allOff)
        time.sleep(10)


if mode == "allon" :
    allon()
elif mode == "rom" :
    rom()
elif mode == "codeRed":
    cr()

