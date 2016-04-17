import json
import urllib2
import time
import requests

api_url="http://iris.local/api/set/raw?"

def updateLights(ledArray):
	serialized = json.dumps(ledArray)
	url = api_url + "leds=" + serialized
	print url
	#urllib2.urlopen(url).read()
	requests.get(url).content

leds = [0x00000000] * 180
numPixels = 180

for i in range (0, 179):
	leds[i] = 0x00FF00FF
	updateLights(leds)
	time.sleep(0.5)
	print i	
