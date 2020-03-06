#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
buzzer = GPIO.PWM(15, 1000)
buzzer.stop()

class Buzzer:

    def success():
        buzzer.stop()
        for i in range(2):
            buzzer.start(50)
            time.sleep(0.05)
            buzzer.stop()
            time.sleep(0.05)
            i-=-1

    def error():
        buzzer.stop()
        for i in range(3):
            buzzer.start(50)
            time.sleep(0.25)
            buzzer.stop()
            time.sleep(0.25)
            i-=-1


#THIS IS ONLY TEST
#try:
#    Buzzer.success()
#    time.sleep(2)
#    Buzzer.error()
#    GPIO.cleanup()
#except KeyboardInterrupt:
#    GPIO.cleanup()