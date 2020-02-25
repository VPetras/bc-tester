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
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

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


class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.app = test_sequence()
        self.dropdown = DropDown()

        for x in module: 
            btn = Button(text = module[x], size_hint_y = None, height = 80,font_size = 30) 
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text)) 
            self.dropdown.add_widget(btn)

        self.mainlabel = Label(text ="HARDWARIO Tester",font_size = 40, size_hint=(1, 0.2), pos_hint={'x':0, 'y':0.8})
        self.githublabel = Label(text ="github.com/VPetras/bc-tester",font_size = 25, size_hint=(1.6, 0.1), pos_hint={'x':0.08, 'y':0})
        self.mainbutton = Button(text ='Choice Modul which you wanna test',font_size = 30, size_hint=(0.3, 0.1), pos_hint={'x':0.01, 'y':0.75})
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)
        self.add_widget(self.mainlabel)
        self.add_widget(self.githublabel)
        self.add_widget(self.mainbutton)

        self.show()
        
    def callback(self, instance, x):
        print("The chosen mode is: {0}".format(x))
        self.app.run(x)
        if x == module['1']:
            sign = {'0':'Status',
                    '1':'Consumpption',
                    '2':'VDD',
                    '3':'TMP112',
                    '4':'ACC',
                    '5':'ATSHA',
                    '6':'RX',
                    '7':'TX',
                    '8':'pins',
                    '9':''}

            data = {'0':'Waiting for start',
                    '1':'No data yet',
                    '2':'No data yet',
                    '3':'No data yet',
                    '4':'No data yet',
                    '5':'No data yet',
                    '6':'No data yet',
                    '7':'No data yet',
                    '8':'No data yet',
                    '9':''}

            status = {'0':['!',[1, 0, 0, 1]],
                    '1':['!',[1, 0, 0, 1]],
                    '2':['!',[1, 0, 0, 1]],
                    '3':['!',[1, 0, 0, 1]],
                    '4':['!',[1, 0, 0, 1]],
                    '5':['!',[1, 0, 0, 1]],
                    '6':['!',[1, 0, 0, 1]],
                    '7':['!',[1, 0, 0, 1]],
                    '8':['!',[1, 0, 0, 1]],
                    '9':['',[1, 0, 0, 1]]}

            self.update(sign, data, status)

            print('1')
        elif x == module['2']:
            self.app.stop()
            print('2')
        elif x == module['3']:
            print('3')
        elif x == module['4']:
            print('4')
        elif x == module['5']:
            print('5')
        elif x == module['6']:
            print('6')
        elif x == module['7']:
            print('7')
        elif x == module['8']:
            print('8')
        elif x == module['9']:
            print('9')

    def show(self):
        
        self.sign0 = Label(text ='',font_size = 35, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.70})
        self.sign1 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.65})
        self.sign2 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.60})
        self.sign3 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.55})
        self.sign4 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.50})
        self.sign5 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.45})
        self.sign6 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.40})
        self.sign7 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.35})
        self.sign8 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.30})
        self.sign9 = Label(text ='',font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.0, 'y':0.25})

        self.add_widget(self.sign0)
        self.add_widget(self.sign1)
        self.add_widget(self.sign2)
        self.add_widget(self.sign3)
        self.add_widget(self.sign4)
        self.add_widget(self.sign5)
        self.add_widget(self.sign6)
        self.add_widget(self.sign7)
        self.add_widget(self.sign8)
        self.add_widget(self.sign9)

        self.data0 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.7})
        self.data1 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.65})
        self.data2 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.60})
        self.data3 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.55})
        self.data4 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.50})
        self.data5 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.45})
        self.data6 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.40})
        self.data7 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.35})
        self.data8 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.30})
        self.data9 = Label(text ='',color=[1, 0.5, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.125, 'y':0.25})

        self.add_widget(self.data0)
        self.add_widget(self.data1)
        self.add_widget(self.data2)
        self.add_widget(self.data3)
        self.add_widget(self.data4)
        self.add_widget(self.data5)
        self.add_widget(self.data6)
        self.add_widget(self.data7)
        self.add_widget(self.data8)
        self.add_widget(self.data9)

        self.status0 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.7})
        self.status1 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.65})
        self.status2 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.60})
        self.status3 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.55})
        self.status4 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.50})
        self.status5 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.45})
        self.status6 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.40})
        self.status7 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.35})
        self.status8 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.30})
        self.status9 = Label(text ='',color=[1, 0, 0, 1],font_size = 30, size_hint=(1, 0.2), pos_hint={'x':0.25, 'y':0.25})

        self.add_widget(self.status0)
        self.add_widget(self.status1)
        self.add_widget(self.status2)
        self.add_widget(self.status3)
        self.add_widget(self.status4)
        self.add_widget(self.status5)
        self.add_widget(self.status6)
        self.add_widget(self.status7)
        self.add_widget(self.status8)
        self.add_widget(self.status9)      

    def update(self, sign, data, status):
        self.sign0.text=sign['0']
        self.sign1.text=sign['1']
        self.sign2.text=sign['2']
        self.sign3.text=sign['3']
        self.sign4.text=sign['4']
        self.sign5.text=sign['5']
        self.sign6.text=sign['6']
        self.sign7.text=sign['7']
        self.sign8.text=sign['8']
        self.sign9.text=sign['9']

        self.data0.text=data['0']
        self.data1.text=data['1']
        self.data2.text=data['2']
        self.data3.text=data['3']
        self.data4.text=data['4']
        self.data5.text=data['5']
        self.data6.text=data['6']
        self.data7.text=data['7']
        self.data8.text=data['8']
        self.data9.text=data['9']

        self.status0.text=status['0'][0]
        self.status0.color=status['0'][1]
        self.status1.text=status['1'][0]
        self.status1.color=status['1'][1]
        self.status2.text=status['2'][0]
        self.status2.color=status['2'][1]
        self.status3.text=status['3'][0]
        self.status3.color=status['3'][1]
        self.status4.text=status['4'][0]
        self.status4.color=status['4'][1]
        self.status5.text=status['5'][0]
        self.status5.color=status['5'][1]
        self.status6.text=status['6'][0]
        self.status6.color=status['6'][1]
        self.status7.text=status['7'][0]
        self.status7.color=status['7'][1]
        self.status8.text=status['8'][0]
        self.status8.color=status['8'][1]
        self.status9.text=status['9'][0]
        self.status9.color=status['9'][1]

class GuiApp(App):

    def build(self):
        return MainScreen()
