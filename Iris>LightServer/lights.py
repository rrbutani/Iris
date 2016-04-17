from dotstar import Adafruit_DotStar

#Setup:
numpixels = 180

datapin   = 26
clockpin  = 19
strip	  = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()
