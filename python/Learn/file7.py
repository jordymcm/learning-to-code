#!/usr/bin/python3

from time import sleep
import os


speed = 1

speed = input ('Speed (1 to 10): ')

speed = 3.1-(int(speed) * 0.3)



yon = 0
while True:
    os.system('clear')
    if yon == 0:
        print (' (#)      _(|)')
        print ('  I         I ')
        print (' /#\\       [#]')
        print ('(###)     _\\/]')
        print (' > |      [   ]')
        print ('   <    <      <')
    else:
        print (' (#)       (|)_')
        print ('  I         I')
        print (' /#\\       [#]')
        print ('(###)      \\/')
        print (' | <       [ ]')
        print (' >         < <')


    yon = 1 -yon
    sleep(speed)
