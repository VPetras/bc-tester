#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown 
from kivy.uix.widget import Widget
from kivy.base import runTouchApp


module = {'1':'Core Module R2.2',
            '2':'Core Module R2.3',
            '3':'Core Module NR',
            '4':'Climate Module',
            '5':'PIR Module',
            '6':'Button Module',
            '7':'LCD Module',
            '8':'CO2 Module',
            '9':'GPS Module',
            '10':'Sensor Module',
            '11':'Relay Module',
            '12':'Encoder Module',
            '13':'Power Module',
            '14':'LoRa Module',
            '15':'Sigfox Module',
            '16':'1-Wire Module',
            '17':'Infra Grid Module',
            '18':'Battery Module',
            '19':'Mini Battery Module',
            '20':'Temperature Tag',
            '21':'Humidity Tag',
            '22':'Barometer Tag',
            '23':'Lux Meter Tag',
            '24':'NFC Tag',
            '25':'VOC Tag',
            '26':'VOC-LP Tag'}

class MainScreen(Widget):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.dropdown = DropDown()

        for x in module: 
            btn = Button(text = module[x], size_hint_y = None, height = 30) 
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text)) 
            self.dropdown.add_widget(btn)

        self.mainlabel = Label(text ="HARDWARIO Tester", size_hint =(0.2, 0.1), pos_hint ={'x':0.01, 'y':0.88})
        self.mainbutton = Button(text ='Choice Modul which you wanna test', size_hint =(0.2, 0.1), pos_hint ={'x':0.01, 'y':0.78})
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)
        self.add_widget(self.mainlabel)
        self.add_widget(self.mainbutton)
    
    def callback(self, instance, x):
        print("The chosen mode is: {0}".format(x))

class TesterApp(App):

    def build(self):
        return MainScreen()

if __name__ == '__main__':
    try:
        TesterApp().run()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)