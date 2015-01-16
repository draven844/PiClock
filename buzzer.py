#Buzzer code for proof of concept prototype 1
#For use in the IB Design Tech IA
#Original source code by Simon Monk for the RPi Starter Kit
#Modified use by Draven Rodriguez

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buzzer_pin = 24

GPIO.setup(buzzer_pin, GPIO.OUT)

def buzz(pitch, duration):
  period = 1.0 / pitch
  delay = period / 2
  cycles = int(duration * pitch)
  for i in range(cycles):
    GPIO.output(buzzer_pin, True)
    time.sleep(delay)
    GPIO.output(buzzer_pin, False)
    time.sleep(delay)