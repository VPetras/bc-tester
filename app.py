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

GPIO.setmode(GPIO.BOARD)

class MyGrid(Widget):
    pass


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
