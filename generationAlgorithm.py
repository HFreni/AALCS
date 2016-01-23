# The purpose of this program is to create an API key & request that is encoded based on a specific seed, either user defined, or autogenerated
# This allows you to provide base64 endcoded API keys and data, with no authentication request being submitted.
# Send two packets of data, an encoded string of data, and your base64 encoded seed. For added security, an API key could be used.
import base64

# Main Encoding Method
def encode(input, seed, apiKey):
    # 1. Encode Input and ApiKey into JSON
    # 2. Encode with the seed given, and parse seed into the data in plaintext.
    # 3. Encode in Base64
    return null

# Main Decoding Method
def decode(input):
    # 1. Separated Data
    # 2. Use Seed to Remove Secondary Encoding, once seed is determined.
    return null

# JSON Sanitizer & Creation Method
def toJSON(data):
    # 1. Populate Data from an array into a JSON file
    # 2. Return structurally sound JSON file
    return null

# Encode Raw Data into B64
def b64E(data):
    # 1. Encode the Base64
    base64.b64encode(data)

# Decode B64 into JSON/Plaintext
def b64D(dataOutput):
    # 1. Decode the Base64
    base64.b64decode(dataOutput)

yobro = base64.b64encode('Andre is a fuckwit')
print(yobro)
print(base64.b64decode(yobro))
