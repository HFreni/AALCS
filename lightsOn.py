import sys
import requests
import time

#TODO: Add All Stuff to Crontab
#Refactor & Add More Modes
#afplay plays music, music solely intended for personal listening, I own a copy, just made it into wav file.
# cron 30 5 * * * wakeup.sh

#Configs
allOn={"power":"on", "color":"rgb:255,255,255", "brightness":1}
allOff={"power":"off"}
rom={"power":"on", "color":"rgb:255,0,0", "brightness":.50}
codeRed={"power":"on", "color":"rgb:255,0,0", "brightness":1}
sleep={"power":"on", "color":"rgb:255,255,255", "brightness":0.25}
dayIsh={"power":"on", "color":"kelvin:3500", "brightness":0.90}
grind={"power":"on", "color":"kelvin:3500","brightness":0.50}
prep={"power":"on", "color":"kelvin:3500","brightness":0.03}

#CLI Tokens
token = sys.argv[1]
mode = sys.argv[2]

#Selector Modes
selector = "all"

#ForDebug
auth = requests.get('https://api.lifx.com/v1/lights/' + selector, auth=(token, ''))

if auth.status_code = "207":
    print("Connected Successfully")
else:
    print("Failed to Connect")

# Main Request Method
def sendReq(payload):
    c = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
    if c.status_code = "207":
        print("Successful")
    else:
        print("Failed")

#Show All Connected Lights
def listlights():
    print auth.status_code
    print auth.content


#Send The Requests Based on CLI Input.
if mode == "allon" :
    sendReq(allOn)
elif mode == "rom":
    sendReq(rom)
elif mode == "list":
    listlights()
elif mode == "night":
    sendReq(allOff)
elif mode == "day":
    sendReq(dayIsh)
elif mode == "school":
    sendReq(allOff)
elif mode == "late":
    sendReq(grind)
elif mode == "prep":
    sendReq(prep)
