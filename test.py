#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init, Fore, Style, Back
import sys

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


def main():
    selected = input(Fore.GREEN + 'Choice Modul which you wanna test (number): ' +Fore.RESET)
    print(Fore.YELLOW + module[selected])
    print(Fore.RED + 'Test COMPLETE'+Fore.GREEN+ ' Succesfull')
    print(Fore.RED + 'Test Failed')


if __name__ == '__main__':
    try:
        init(autoreset=True)
        for x in module:
            print(Fore.BLUE+"{:02d} - ".format(int(x)) + Fore.RESET+module[x])
        while True:
            main()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)
