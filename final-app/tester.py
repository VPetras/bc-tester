#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generic
import os
import sys
import threading
import time
#kivy
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
#test sequences
from CoreModuleR22 import CoreModuleR22
from CoreModuleR23 import CoreModuleR23
from CoreModuleNR import CoreModuleNR
from ClimateModule import ClimateModule
from PIRModule import PIRModule
from ButtonModule import ButtonModule
from LCDModule import LCDModule
from CO2Module import CO2Module
from GPSModule import GPSModule
from SensorModule import SensorModule
from RelayModule import RelayModule
from EncoderModule import EncoderModule
from PowerModule import PowerModule
from LoRaModule import LoRaModule
from SigfoxModule import SigfoxModule
from OneWireModule import OneWireModule
from InfraGridModule import InfraGridModule
from BatteryModule import BatteryModule
from MiniBatteryModule import MiniBatteryModule
from TemperatureTag import TemperatureTag
from HumidityTag import HumidityTag
from BarometerTag import BarometerTag
from LuxMeterTag import LuxMeterTag
from NFCTag import NFCTag
from VOCTag import VOCTag
from VOC_LPTag import VOC_LPTag

class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.dropdown = DropDown()

        self.thread = None
        self.started = False
        self.testing_module = ''

        self.module = {'1':'Core Module R2.2',
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

        self.testing_sequence = {'Core Module R2.2': 'CoreModuleR22',
                                'Core Module R2.3': 'CoreModuleR23',
                                'Core Module NR': 'CoreModuleNR',
                                'Climate Module': 'ClimateModule',
                                'PIR Module': 'PIRModule',
                                'Button Module': 'ButtonModule',
                                'LCD Module': 'LCDModule',
                                'CO2 Module': 'CO2Module',
                                'GPS Module': 'GPSModule',
                                'Sensor Module': 'SensorModule',
                                'Relay Module': 'RelayModule',
                                'Encoder Module': 'EncoderModule',
                                'Power Module': 'PowerModule',
                                'LoRa Module': 'LoRaModule',
                                'Sigfox Module': 'SigfoxModule',
                                '1-Wire Module': 'OneWireModule',
                                'Infra Grid Module': 'InfraGridModule',
                                'Battery Module': 'BatteryModule',
                                'Mini Battery Module': 'MiniBatteryModule',
                                'Temperature Tag': 'TemperatureTag',
                                'Humidity Tag': 'HumidityTag',
                                'Barometer Tag': 'BarometerTag',
                                'Lux Meter Tag': 'LuxMeterTag',
                                'NFC Tag': 'NFCTag',
                                'VOC Tag': 'VOCTag',
                                'VOC-LP Tag': 'VOC_LPTag'}

        self.sign = {'0':['Status',[1, 1, 1, 1]],
                     '1':['',[1, 1, 1, 1]],
                     '2':['',[1, 1, 1, 1]],
                     '3':['',[1, 1, 1, 1]],
                     '4':['',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}

        self.data = {'0':['Waiting for choice module',[1, 1, 1, 1]],
                     '1':['',[1, 1, 1, 1]],
                     '2':['',[1, 1, 1, 1]],
                     '3':['',[1, 1, 1, 1]],
                     '4':['',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}

        self.status = {'0':['',[1, 0, 0, 1]],
                       '1':['',[1, 0, 0, 1]],
                       '2':['',[1, 0, 0, 1]],
                       '3':['',[1, 0, 0, 1]],
                       '4':['',[1, 0, 0, 1]],
                       '5':['',[1, 0, 0, 1]],
                       '6':['',[1, 0, 0, 1]],
                       '7':['',[1, 0, 0, 1]],
                       '8':['',[1, 0, 0, 1]],
                       '9':['',[1, 0, 0, 1]]}

        for x in self.module: 
            btn = Button(text = self.module[x], size_hint_y = None, height = 80,font_size = 30) 
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text)) 
            self.dropdown.add_widget(btn)

        self.mainlabel = Label(text ="HARDWARIO Tester",font_size = 40, size_hint=(1, 0.2), pos_hint={'x':0, 'y':0.8})
        self.githublabel = Label(text ="github.com/VPetras/bc-tester",font_size = 25, size_hint=(1.6, 0.1), pos_hint={'x':0.08, 'y':0})
        self.mainbutton = Button(text ='Choice Modul which you wanna test',font_size = 30, size_hint=(0.3, 0.1), pos_hint={'x':0.01, 'y':0.75})
        self.button = Button(text ='end testing',font_size = 30, size_hint=(0.3, 0.1), pos_hint={'x':0.35, 'y':0.01})
        self.button.bind(on_press = self.stop_btn)
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)
        self.add_widget(self.mainlabel)
        self.add_widget(self.githublabel)
        self.add_widget(self.mainbutton)
        self.add_widget(self.button)
        self.button.disabled=True

        self.show()
        self.update()
    
    def threaded_program(self):
        self.mainbutton.disabled = True
        self.button.disabled = False
        self.running = True

        print(self.testing_module)
        seq = self.testing_sequence[self.testing_module]
        print(seq)
        print(self.sign)
        seq = globals()[seq]()
        self.sign = seq.sign
        self.update()
        print(self.sign)

        while self.started:
            print("running module test")

            self.sign = seq.sign
            self.update()

            seq.test0()

            time.sleep(1)

            self.data = seq.data
            self.update()

            seq.test1()
            time.sleep(1)

            self.data = seq.data
            self.update()

            seq.test2()
            time.sleep(1)

            self.data = seq.data
            self.update()

            seq.test3()
            time.sleep(1)

            self.data = seq.data
            self.update()

            time.sleep(1)
            seq.clean()
            self.data = seq.data
            self.update()

            time.sleep(1)
   
        self.running = False
        print('thread is gone')
        self.mainbutton.disabled = False
        self.button.disabled=True
        self.erase()

    def stop(self):
        print("stoping module test")
        self.started = False

    def start(self):
        if(self.started != True):
            print('starting thread')
            self.started = True
            self.thread = threading.Thread(target=self.threaded_program, args=())
            self.thread.start()

    def stop_btn(self, x):
        print(x.text)
        self.stop()

    def callback(self, instance, x):
        for i in range(len(self.module)):
            if x == self.module[str(i+1)]:
                print(self.module[str(i+1)])
                self.testing_module = x
                self.start()

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

    def update(self):

        self.sign0.text=self.sign['0'][0]
        self.sign1.text=self.sign['1'][0]
        self.sign2.text=self.sign['2'][0]
        self.sign3.text=self.sign['3'][0]
        self.sign4.text=self.sign['4'][0]
        self.sign5.text=self.sign['5'][0]
        self.sign6.text=self.sign['6'][0]
        self.sign7.text=self.sign['7'][0]
        self.sign8.text=self.sign['8'][0]
        self.sign9.text=self.sign['9'][0]

        self.data0.text=self.data['0'][0]
        self.data1.text=self.data['1'][0]
        self.data2.text=self.data['2'][0]
        self.data3.text=self.data['3'][0]
        self.data4.text=self.data['4'][0]
        self.data5.text=self.data['5'][0]
        self.data6.text=self.data['6'][0]
        self.data7.text=self.data['7'][0]
        self.data8.text=self.data['8'][0]
        self.data9.text=self.data['9'][0]

        #for i in range(10):
        #    data = getattr(self, 'data{}'.format(i))
        #    assert data
        #    data.text = self.data[str(i)]

        self.status0.text=self.status['0'][0]
        self.status0.color=self.status['0'][1]
        self.status1.text=self.status['1'][0]
        self.status1.color=self.status['1'][1]
        self.status2.text=self.status['2'][0]
        self.status2.color=self.status['2'][1]
        self.status3.text=self.status['3'][0]
        self.status3.color=self.status['3'][1]
        self.status4.text=self.status['4'][0]
        self.status4.color=self.status['4'][1]
        self.status5.text=self.status['5'][0]
        self.status5.color=self.status['5'][1]
        self.status6.text=self.status['6'][0]
        self.status6.color=self.status['6'][1]
        self.status7.text=self.status['7'][0]
        self.status7.color=self.status['7'][1]
        self.status8.text=self.status['8'][0]
        self.status8.color=self.status['8'][1]
        self.status9.text=self.status['9'][0]
        self.status9.color=self.status['9'][1]
        
    def erase(self):
        for i in range(10):
            self.sign[str(i)][0] = ''
            self.data[str(i)][0] = ''
            self.status[str(i)][0] = ''
        self.sign['0'][0] = 'Status'
        self.data['0'][0] = 'Waiting for choice module'
        self.update()

class GuiApp(App):

    def build(self):
        return MainScreen()
        
if __name__ == '__main__':
    try:
        GuiApp().run()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)