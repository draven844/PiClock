# Alarm Clock with Tranceiver
# Modified by Draven Rodriguez
# Modified from Ismail Uddin's code
# For use in Draven Rodriguez's IBDT Design Project
#Do NOT run in Python 3, use regular IDLE
#8 hours work on 1-15-15

import time
import RPi.GPIO as GPIO
from buzzer import buzz
from trigger import trigger

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
awake = 0
run = 1
try:
    # Loop to continuously check time, buzz the buzzer for the set alarm time
    while run == 1:
	#This polls the user for the time in which they want the alarm to go off
		response = raw_input("Please input the time for the alarm in military format HHMM: \n")
		print("Alarm has been set for %s hrs" % response)
		alarm = int(response)
		
            # Continually gets the time as an integer value
		curr_time = int(time.strftime("%H%M"))

            # Buzzes the buzzer when the time reaches the set alarm time
		if curr_time == alarm:
            buzz(10,0.5)
            time.sleep(0.25)
            awake = 1
					
            # Snoozes the alarm for 8 minutes from the current time
            # Only works whilst the alarm is going off
        if GPIO.input(25) == 1 and awake == 1:
            trigger()
			awake = 0
            run = 0
            print("Alarm has been silenced. Devices will power on.")
					
			# If alarm continues past the set alarm time without being
            # snoozed, the alarm time is changed to the current time.
            # This ensures the alarm buzzes continuously until the
            # snooze button is pressed.
        elif curr_time != alarm and awake == 1:
            alarm = curr_time
            buzz(10,0.5)
		    time.sleep(0.25)

	#This follows the button press. It'll send another signal when activated and go back to the beginning of the following while
    while run == 0:
        input("Press enter to send another signal and turn off the relay.")
		trigger()
		run = 1
finally:
        GPIO.cleanup()
	print("End")
