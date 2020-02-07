#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import RPi.GPIO as GPIO
from led import Led

red = Led(37)
green = Led(33)
blue = Led(35)
yellow = Led(31)

class MyGrid(Widget):
    def red_on(self):
        red.on()

    def red_off(self):
        red.off()

    def green_on(self):
        green.on()

    def green_off(self):
        green.off()

    def blue_on(self):
        blue.on()

    def blue_off(self):
        blue.off()

    def yellow_on(self):
        yellow.on()

    def yellow_off(self):
        yellow.off()


class MyApp(App): # <- Main Class
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    try:
        MyApp().run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        GPIO.cleanup()
        sys.exit(1)
