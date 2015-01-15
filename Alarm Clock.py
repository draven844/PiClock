#Alarm Clock.py
#For use with Draven Rodriguez's IB Design Tech IA
#Modified from Science Exposure's RPi Alarm Clock Code
#Modified by Draven Rodriguez

import time
import RPi.GPIO as GPIO
from buzzer import buzz

while True:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO,IN, pull_up_down=GPIO.PUD_UP)

	response = input("Input the time for the alarm in HHMM format using 24 hr. military time: \n")
	#find way to validate user input as being in proper format
	print("The alarm has been set for %s hours" % response)
	buzz(500,0.1)

	alarm = int(response)
	awake = 0
	print ("\n")
	print ("The alarm has been shut off. \n Press \"Enter\" to turn the light off and restart the program.\n")
	input("Awaiting keystroke...")