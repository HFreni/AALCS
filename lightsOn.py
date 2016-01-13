import sys
import requests
import time

#TODO: Add All Stuff to Crontab
#Refactor & Add More Modes
#afplay plays music, music solely intended for personal listening, I own a copy, just made it into wav file.
#Clean This Shit Up
# cron 30 5 * * * wakeup.sh

#Configs
allOn={"power":"on", "color":"rgb:255,255,255", "brightness":1}
allOff={"power":"off"}
rom={"power":"on", "color":"rgb:255,0,0", "brightness":.50}
codeRed={"power":"on", "color":"rgb:255,0,0", "brightness":1}
sleep={"power":"on", "color":"rgb:255,255,255", "brightness":0.25}
dayIsh={"power":"on", "color":"kelvin:3500", "brightness":0.90}
grind={"power":"on", "color":"kelvin:3500","brightness":"0.50"}

#CLI Tokens
token = sys.argv[1]
mode = sys.argv[2]

#Selector Modes
selector = "all"

#ForDebug
auth= requests.get('https://api.lifx.com/v1/lights/' + selector, auth=(token, ''))

# Main Request Method
def sendReq(payload):
    c = requests.put('https://api.lifx.com/v1/lights/' + selector + '/state', data=payload, auth=(token, ''))
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
        time.sleep(2)
        sendReq(allOff)
        time.sleep(2)

def nightTime():
    sendReq(sleep)
    time.sleep(240)
    sendReq(allOff)

def dayTime():
    sendReq(dayIsh)

def school():
    sendReq(allOff)

def nightGrind():
    sendReq(grind)

def listlights():
    print auth.status_code
    print auth.content

if mode == "allon" :
    lightsOn()
elif mode == "rom" :
    romA()
elif mode == "codeRed":
    cr()
elif mode == "list":
    listlights()
elif mode == "night":
    nightTime()
elif mode == "day":
    dayTime()
elif mode == "school":
    school()
elif mode == "late":
    nightGrind()
