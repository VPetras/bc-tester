#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Led:

  def __init__(self, gpio):
    self.gpio = gpio
    self.state = 0
    GPIO.setup(self.gpio, GPIO.OUT)
    GPIO.output(self.gpio, 1)

  def on(self):
    GPIO.output(self.gpio, 0)
    self.state = 0

  def off(self):
    GPIO.output(self.gpio, 1)
    self.state = 1

#THIS IS ONLY TEST
#try:
# red = Led(37)
# green = Led(33)
# blue = Led(35)
# yellow = Led(31)
# while True:
#  red.on()
#  green.off()
#  blue.off()
#  yellow.off()
#  print('red')
#  time.sleep(1)
#  red.off()
#  green.on()
#  blue.off()
#  yellow.off()
#  print('green')
#  time.sleep(1)
#  red.off()
#  green.off()
#  blue.on()
#  yellow.off()
#  print('blue')
#  time.sleep(1) 
#  red.off()
#  green.off()
#  blue.off()
#  yellow.on()
#  print('yellow')
#  time.sleep(1)   
#except KeyboardInterrupt:
# GPIO.cleanup()