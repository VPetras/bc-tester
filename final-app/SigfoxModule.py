#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SigfoxModule():

    def __init__(self):
        self.sign = {'0':['Status',[1, 1, 1, 1]],
                     '1':['VDD',[1, 1, 1, 1]],
                     '2':['Consumption',[1, 1, 1, 1]],
                     '3':['Temperature',[1, 1, 1, 1]],
                     '4':['',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}
        
        self.data = {'0':['Waiting fot start',[1, 1, 1, 1]],
                     '1':['No data yet',[1, 1, 1, 1]],
                     '2':['No data yet',[1, 1, 1, 1]],
                     '3':['No data yet',[1, 1, 1, 1]],
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
        
        self.min_VDD = 3
        self.max_VDD = 3.3
        self.min_consumption = 1.3
        self.max_consumption = 2.3
        self.min_temp = 21
        self.max_temp = 25

    def clean(self):
        self.sign = {'0':['Status',[1, 1, 1, 1]],
                     '1':['VDD',[1, 1, 1, 1]],
                     '2':['Consumption',[1, 1, 1, 1]],
                     '3':['Temperature',[1, 1, 1, 1]],
                     '4':['',[1, 1, 1, 1]],
                     '5':['',[1, 1, 1, 1]],
                     '6':['',[1, 1, 1, 1]],
                     '7':['',[1, 1, 1, 1]],
                     '8':['',[1, 1, 1, 1]],
                     '9':['',[1, 1, 1, 1]]}
        
        self.data = {'0':['Waiting fot start',[1, 1, 1, 1]],
                     '1':['No data yet',[1, 1, 1, 1]],
                     '2':['No data yet',[1, 1, 1, 1]],
                     '3':['No data yet',[1, 1, 1, 1]],
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
        
    def test0(self):
        print('test0')
        self.data['0'][0] = 'Testing'

    def test1(self):
        print('test1')
        Volts = 3.235
        self.data['1'][0] = '3.245 V'

    def test2(self):
        print('test2')
        uAmp = 2.3
        self.data['2'][0] = '2.3 uA'

    def test3(self):
        print('test3')
        Temp = 26.5
        self.data['3'][0] = '15 °C'

    def test4(self):
        print('test4')
        pass

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