import requests

#API Tokens
token = #TOKEN

#Global Variables
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

turnOn = {"power":"on", "color":"kelvin:3500", "brightness":1}

sendReq(turnOn)
