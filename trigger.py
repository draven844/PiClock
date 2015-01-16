# Trigger Script for Draven Rodriguez's IBDT Project
# Script modified from Simon Monk's 'Pi Starter Kit' repo

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger_pin = 23

GPIO.setup(trigger_pin, GPIO.OUT)

def trigger():
   GPIO.output(trigger_pin, True)
   time.sleep(delay)
   GPIO.output(trigger_pin, False)
   time.sleep(delay)