import RPi.GPIO as GPIO
import pprint
import time

GPIO.setwarnings(False)

pin_in_other = 17 #0
pin_in = 0 #7
pin_out = 25 #6

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input and one output
GPIO.setup(pin_in, GPIO.IN)
#GPIO.setup(pin_in_other, GPIO.IN)
#GPIO.setup(pin_out, GPIO.OUT)

while(True):
	# input from pin_in
	input_value = GPIO.input(pin_in)
	print(input_value)
	#input_value_2 = GPIO.input(pin_in_other)
	# output to pin_out
	if True == input_value:
		#GPIO.output(pin_out, False)
		pprint.pprint("Yep (1)")
	#elif True == input_value_2:
	#	GPIO.output(pin_out, False)
	#	pprint.pprint("Yep (2)")
	else:
		#GPIO.output(pin_out, True)
		pprint.pprint("Nope")
	time.sleep(1)
