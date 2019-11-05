import urllib.parse
import urllib.request
import json
import os

clear = lambda: os.system('cls') #on Windows System
clear()

response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')

obj = json.loads(response.read())

#print (obj)
print (obj['iss_position']['latitude'], obj['iss_position']['longitude'])

# Example prints:
#   1364795862
#   -47.36999493 151.738540034