#!/usr/bin/python3

from time import sleep
import os


yon = 0
while True:
    os.system('clear')
    if yon == 0:
        print (' (#)')
        print ('  I ')
        print (' /#\\')
        print ('(###)')
        print (' > |')
        print ('   <')
        yon =1
    else:
        print (' (#)')
        print ('  I ')
        print (' /#\\')
        print ('(###)')
        print (' | <')
        print (' >')
        yon =0
    sleep(1)
