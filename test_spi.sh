#!/bin/bash

# MOSI (master output, slave input) -> MISO (master input, slave output)

sudo ./spidev_test -D /dev/spidev0.0^

#pi@raspberrypi ~/Code $ sudo ./spidev_test -D /dev/spidev0.0
#spi mode: 0
#bits per word: 8
#max speed: 500000 Hz (500 KHz)
#
#FF FF FF FF FF FF 
#40 00 00 00 00 95 
#FF FF FF FF FF FF 
#FF FF FF FF FF FF 
#FF FF FF FF FF FF 
#DE AD BE EF BA AD 
#F0 0D 
