#!/usr/bin/python3
from led import Led
import RPi.GPIO as GPIO

red = Led(37)
green = Led(33)
blue = Led(35)
yellow = Led(31)


try:
    while True:
        red.on()
        green.on()
        blue.off()
        yellow.off()

except KeyboardInterrupt:
    GPIO.cleanup()