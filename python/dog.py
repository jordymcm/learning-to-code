#!/usr/bin/python3

from time import sleep
from getch import getch
import os

Onof =0
while True:

    if Onof == 0:
        print ('              |-----|')
        print ('              |-----|')
        print ('    /---------\\       ')
        print ('___|          /')
        print ('   \\---------/')
    else:
        print ('              |-----|')
        print ('              |-----|')
        print ('    /---------\\       ')
        print ('___|          /')
        print ('   \\---------/')
        print (' ______________')
        print ('/              \\')



    if (getch() == 's'):
        os.system('clear')
        Onof = 1 - Onof
