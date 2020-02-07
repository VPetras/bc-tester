#!/usr/bin/python3
#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
Window.fullscreen = False


class MyScreenManager(ScreenManager):
    pass


class LoginScreen(Screen):

    def check_password(self, instance, password):
        if password == "pwd":
            instance.current = "screen2"


class Screen2(Screen):
    pass


class TestApp(App):
    title = "HARDWARIO Tester 1.0"

    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    Config.set('graphics', 'fullscreen', 'fake')
    Config.set('graphics', 'window_state', 'visible') 
    TestApp().run()