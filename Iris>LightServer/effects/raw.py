def info():
	print "Hai"

def run(strip, params):
	print "Hai2"
	print vars(params)
#	print vars(strip)
	for i in range(0, strip.numPixels()):
		strip.setPixelColor(i, strip.getPixelColor(i) + 10)
		print i
		strip.show()
