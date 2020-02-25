#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time

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


class test:

    def __init__(self):
        self.thread = None
        self.started = False
        self.running = False
        self.module = ''

    def threaded_program(self):
        self.running = True
        while self.started:
            print("running {}. module test".format(self.module))
            print('1')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('4')
            time.sleep(1)
            print('5')
            time.sleep(1)
            print('6')
            time.sleep(1)
            print('7')
            time.sleep(1)
            print('8')
            time.sleep(1)
        self.running = False
        print('thread is gone')

    def run(self, module):
        if(self.started != True):
            print('starting thread')
            self.started = True
            self.module = module
            self.thread = threading.Thread(target=self.threaded_program, args=())
            self.thread.start()

    def stop(self):
        print("stoping {}. module test".format(self.module))
        self.started = False
        #self.thread.join()
