def info():
	print "Hai"

def run(strip, params):
	print "Hai2"
	print vars(params)
	for i in range(0, strip.numPixels):
		strip.set(i, 0x00FFFFFF)
	strip.show()