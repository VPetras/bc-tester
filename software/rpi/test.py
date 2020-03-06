#!/usr/bin/python3
from led import Led
from buzzer import Buzzer
import RPi.GPIO as GPIO
import time

red = Led(37)
green = Led(33)
blue = Led(35)
yellow = Led(31)


try:
    while True:
        red.off()
        green.on()
        blue.off()
        yellow.off()
        Buzzer.success()
        time.sleep(2)
        red.on()
        green.off()
        blue.off()
        yellow.off()
        Buzzer.error()
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()