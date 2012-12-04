import RPi.GPIO as GPIO
import pprint
import time
import numpy

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:   
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout /= 2       # first bit is 'null' so drop it
        return adcout

results = numpy.array([])
while(True):
	# input from pin_in
	#in = GPIO.input(SPIMISO)
        x = readadc(6, SPICLK, SPIMOSI, SPIMISO, SPICS)
	#moving average
	w = numpy.ones( x, 'd')
	#other windows
	s = numpy.array( x )
	#hanning
	#w = numpy.hanning(s)
	#hamming
	#w = numpy.hamming(s)
	#bartlett
	#w = numpy.bartlett(s)
	#blackman
	#w = numpy.blackman(s)
	#kaiser
	#w = numpy.kaiser(s, beta = 14)

	print('current', x, 'running', results.mean(), results.std() )
	if x > ( results.mean() - ( 3 * results.std() ) ) and x < ( results.mean() + ( 3 * results.std() ) ):
		print("OK", x)
	elif x > ( results.mean() + ( 3 * results.std() ) ):
		print("TOO BIG", results.mean() + ( 3 *  results.std() ) )
	elif x < ( results.mean() + ( 3 * results.std() ) ):
		print("TOO SMALL", results.mean() + ( 3 *  results.std() ) )
	y = numpy.convolve(w/w.sum(),x,mode='valid')
	results = numpy.append( results, y.sum() )


	#print(s);
	#if 0 != s:
	#	pprint.pprint("Movement: " + str(s))
	time.sleep(1)


