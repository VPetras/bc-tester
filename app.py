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
from led import Led



class MyGrid(Widget):
    pass


class MyApp(App): # <- Main Class
    def build(self):
        red = Led(37)
        green = Led(33)
        blue = Led(35)
        yellow = Led(31)
        return MyGrid()

if __name__ == '__main__':
    try:
        MyApp().run()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)
