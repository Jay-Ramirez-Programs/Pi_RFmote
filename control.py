#!/usr/bin/env python
"""Provides an interface to control Cos Electronics RF remote over I2C.

When program is run, it asks the user for a command to send to the RF node.
"""
import smbus
import time

__author__ = "Jay Ramirez"
__copyright__ = "Copyright 2020, Jay Ramirez"
__credits__ = ["Jay Ramirez", "Sukhi Grewal"]
__license__ = "GNU"
__version__ = "3.0"
__maintainer__ = "Jay Ramirez"
__email__ = "JayRamirez@TAMU.edu"
__status__ = "Development"

DEVICE_ADDRESS = 0x69
DEVICE_REG_MODE1= 0x00

while(1):
    print("RF Light Switch")
    print("Cos Electronics")
    print(" ")
    print("Copyright 2020")

    for x in range (0, 15):
        print(" ")

    bus = smbus.SMBus(1)
    initialStatus = bus.read_byte(0x69)

    if initialStatus == 10:
        	print("Light is connected but no information is available.")
    elif initialStatus == 47:
        	print("Cannot establish radio link with light.")
    elif initialStatus == 39:
	    print("Light is at maximum brightness.")
    elif initialStatus == 20:
	    print("Light is currently off.")
    elif initialStatus == 21:
	    print("Light is at half brightness.")
    elif initialStatus == 30:
	    print("Light is at minimum brightness.")
    print(" ")
    print("Enter command to send to the light.")
    print("(c for command list)")
    userInput = raw_input()

    if userInput == "c":
            #Display command list
	    for x in range (0, 5):
		    print(" ")

	    print("Command List:")
            print(" ")
            print("on: Turn lights on")
	    print("off: Turn lights off")
	    print("max: Maximum brightness")
	    print("min: Minimum brightness")
    elif userInput == "on":
	    bus.write_byte(0x69, 21)
    elif userInput == "off":
	    bus.write_byte(0x69, 20)
    elif userInput == "max":
    	    bus.write_byte(0x69, 39)
    elif userInput == "min":
	    bus.write_byte(0x69, 30)
    else:
	    print("Cannot understand " + str(userInput))

    if userInput == "c":
	    print(" ")
    else:
	    msg=bus.read_byte(0x69)
	    print(" ")

	    if msg == 47:
		    print("Light is unreachable.")
	    elif msg == 39:
		    print("Light is very bright!")
	    elif msg == 20:
		    print("Light is off.")
	    elif msg == 21:
		    print("Light is at 50 percent.")
	    elif msg == 30:
		    print("Light is at minimum brightness.")
	    else:
		    print("Light status is: " + str(msg))

    bus.close()
