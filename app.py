#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import *
from kivy.config import Config

class MyApp(App):
    #Metoda, která vrátí tlačítko, které se má zobrazit
    def build(self):
        return Button(text = "Hello World!")


if __name__ == "__main__":
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    MyApp().run()