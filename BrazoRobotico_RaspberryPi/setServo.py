#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)
p = GPIO.PWM(24, 50)
dc = 3
p.start(dc)
p.ChangeDutyCycle(dc)
time.sleep(2)
