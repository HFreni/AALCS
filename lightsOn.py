import sys
import requests
import time

#TODO: Add json & base64 decoder so I can somewhat securely store data on the server's side.
#TODO: Migrate this to a backend system, so I can make personal API calls to a server.

#Light Configurations
allOn={"power":"on", "color":"rgb:255,255,255", "brightness":1}
allOff={"power":"off"}
rom={"power":"on", "color":"rgb:255,0,0", "brightness":.50}
codeRed={"power":"on", "color":"rgb:255,0,0", "brightness":1}
sleep={"power":"on", "color":"rgb:255,255,255", "brightness":0.25}
dayIsh={"power":"on", "color":"kelvin:3500", "brightness":0.90}
grind={"power":"on", "color":"kelvin:3500","brightness":0.50}
prep={"power":"on", "color":"kelvin:3500","brightness":0.03}

#CLI Tokens
token = #TOKEN

#Global Variables Modes
apiURL = 'https://api.lifx.com/v1/lights/'
connectorSegment = '/state'
selector = 'all'

#ForDebug
auth = requests.get(apiURL + selector, auth=(token, ''))

if auth.status_code == 200:
    print("Connected Successfully")
else:
    print("Failed to Connect")

# Main Request Method
def sendReq(payload):
    c = requests.put(apiURL + selector + connectorSegment, data=payload, auth=(token, ''))
    if c.status_code == 207:
        print("Successful")
    else:
        print("Failed")

#Show All Connected Lights
def listlights():
    print auth.status_code
    print auth.content

mode = input("Set Light Mode, It can be:\nallon\nrom\nlist\nnight\nday\nschool\nlate\nprep")

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
