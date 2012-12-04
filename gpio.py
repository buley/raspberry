import RPi.GPIO as GPIO
import pprint

GPIO.setwarnings(False)

pin_in_other = 17 #0
pin_in = 4 #7
pin_out = 25 #6

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# set up the GPIO channels - one input and one output
GPIO.setup(pin_in, GPIO.IN)
GPIO.setup(pin_in_other, GPIO.IN)
GPIO.setup(pin_out, GPIO.OUT)

# input from pin_in
input_value = GPIO.input(pin_in)
input_value_2 = GPIO.input(pin_in_other)

# output to pin_out
if input_value or input_value_2:
	GPIO.output(pin_out, True)
else:
	GPIO.output(pin_out, False)
