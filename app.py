#!/usr/bin/python3
#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'fullscreen', '0')
Config.write()


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
    TestApp().run()