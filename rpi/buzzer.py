#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)

def success():
    p = GPIO.PWM(15, 1000)
    p.stop()
    for i in range(2):
        p.start(50)
        time.sleep(0.05)
        p.stop()
        time.sleep(0.05)
        i-=-1

def error():
    p = GPIO.PWM(15, 10000)
    p.stop()
    for i in range(2):
        p.start(50)
        time.sleep(0.25)
        p.stop()
        time.sleep(0.25)
        i-=-1



try:
    success()
    time.sleep(2)
    error()
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()

