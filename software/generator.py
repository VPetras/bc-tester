#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
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


if os.path.isfile('filename.txt'):
    print ("File exist")
else:
    print ("File not exist")

data = {}
string = ''
for i in range(len(module)):
    print(i)
    n = module[str(i+1)]
    print(n)
    m = n.replace(' ', '')
    m = m.replace('.', '')
    m = m.replace('-', '_')
    print(m)
    string = string + 'from ' + m + ' import ' + m + '\n'
#    data[n] = m
#    path = "{:s}.py".format(m)
#    if os.path.isfile(path):
#        print ("File exist")
#    else:
#        print ("File not exist")
#        f = open(path, "x")
#        f.close()
#f = open("data.txt", "x")
#f.write(str(data))
#f.close()
f = open("data.txt", "a")
f.write(string)
f.close()
