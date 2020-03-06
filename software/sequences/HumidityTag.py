#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ADS1115
from sht20 import SHT20
import time

class HumidityTag():

    def __init__(self):
        self.sign = {'0':['Status',[1, 1, 1, 1]],
                     '1':['VDD',[1, 1, 1, 1]],
                     '2':['Consumption',[1, 1, 1, 1]],
                     '3':['Temperature',[1, 1, 1, 1]],
                     '4':['Humidity',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}
        
        self.data = {'0':['Waiting fot start',[1, 1, 1, 1]],
                     '1':['No data yet',[1, 1, 1, 1]],
                     '2':['No data yet',[1, 1, 1, 1]],
                     '3':['No data yet',[1, 1, 1, 1]],
                     '4':['No data yet',[1, 1, 1, 1]],
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

        self.ads = ADS1115.ADS1115(address=0x48)
        self.sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit)
        
        self.MIN_VDD = 3
        self.MAX_VDD = 3.3
        self.MIN_CONSUMPTION = 1.3
        self.MAX_CONSUMPTION = 2.3
        self.MIN_TEMP = 20
        self.MAX_TEMP = 25
        self.MIN_HUM = 20
        self.MAX_HUM = 40

    def clean(self):
        self.sign = {'0':['Status',[1, 1, 1, 1]],
                     '1':['VDD',[1, 1, 1, 1]],
                     '2':['Consumption',[1, 1, 1, 1]],
                     '3':['Temperature',[1, 1, 1, 1]],
                     '4':['Humidity',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}
        
        self.data = {'0':['Waiting fot start',[1, 1, 1, 1]],
                     '1':['No data yet',[1, 1, 1, 1]],
                     '2':['No data yet',[1, 1, 1, 1]],
                     '3':['No data yet',[1, 1, 1, 1]],
                     '4':['No data yet',[1, 1, 1, 1]],
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
        
    def test0(self):
        print('test0')
        self.data['0'][0] = 'Testing'

    def test1(self):
        print('test1')

        Volts = 0
        arith = 5
        try:
            for i in range(arith):
                volt = self.ads.readADCSingleEnded(channel=0, pga=6144, sps=860)
                Volts = Volts + volt
                print("{:.3f} V ".format(volt/1000))
                time.sleep(0.1)
            Volts = Volts / (arith * 1000)
        except Exception as e:
            print('Exited with error: {}'.format(e))

        self.data['1'][0] = '{:.2f} V'.format(Volts)
        if Volts >= self.MIN_VDD and Volts <= self.MAX_VDD:
            self.status['1'][0] = 'OK'
            self.status['1'][1] = [0,1,0,1]
        else:
            self.status['1'][0] = 'NOK'
            self.status['1'][1] = [1,0,0,1]

    def test2(self):
        print('test2')
        uAmp = 2.3
        self.data['2'][0] = '{:.1f} uA'.format(uAmp)
        if uAmp >= self.MIN_CONSUMPTION and uAmp <= self.MAX_CONSUMPTION:
            self.status['2'][0] = 'OK'
            self.status['2'][1] = [0,1,0,1]
        else:
            self.status['2'][0] = 'NOK'
            self.status['2'][1] = [1,0,0,1]

    def test3(self):
        print('test3')
        Temp = self.sht.read_temp()
        self.data['3'][0] = '{:.2f} °C'.format(Temp)
        if Temp >= self.MIN_TEMP and Temp <= self.MAX_TEMP:
            self.status['3'][0] = 'OK'
            self.status['3'][1] = [0,1,0,1]
        else:
            self.status['3'][0] = 'NOK'
            self.status['3'][1] = [1,0,0,1]

    def test4(self):
        print('test4')
        Hum = self.sht.read_humid()
        self.data['4'][0] = '{:.2f} °C'.format(Hum)
        if Hum >= self.MIN_HUM and Hum <= self.MAX_HUM:
            self.status['4'][0] = 'OK'
            self.status['4'][1] = [0,1,0,1]
        else:
            self.status['4'][0] = 'NOK'
            self.status['4'][1] = [1,0,0,1]

    def test5(self):
        print('test5')
        pass

    def test6(self):
        print('test6')
        pass

    def test7(self):
        print('test7')
        pass
    
    def test8(self):
        print('test8')
        pass

    def test9(self):
        print('test9')
        pass