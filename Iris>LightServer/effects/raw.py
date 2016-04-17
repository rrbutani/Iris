import json

original_errmsg= json.decoder.errmsg

def our_errmsg(msg, doc, pos, end=None):
    json.last_error_position= json.decoder.linecol(doc, pos)
    return original_errmsg(msg, doc, pos, end)

json.decoder.errmsg= our_errmsg

def info():
	print "Hai"

def run(strip, params):
#	print "Hai2"
	rawJSON = params['leds']
#	print rawJSON
	try:	
		leds = json.loads(rawJSON)
		print "processed"
	except ValueError as e:
#		print "you dead"	
		print("error at")#, json.last_error_position)
	except:
		print "you still dead"
	print "Stuff: "
#	print  leds
#	print type(leds)
#	print type(rawJSON)
#	print (leds[1])
#	print "Hai3"
#	return leds
#	type(leds)
	for i in range(0, len(leds)):
#		print i
		strip.setPixelColor(i, leds[i])
#		print i, leds[i]
	strip.show()
