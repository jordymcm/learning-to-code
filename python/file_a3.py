#!/usr/bin/python3

from getch import getch
import os
import sys

y = 0
x = 0
c = '.'

while True:
    if (x < 0):
        x = 1

    ch = getch()
    if (ch == 'w'):
        os.system('clear')
        y = y + 1
        for i in range (10):
            if i == x:
                sys.stdout.write('@')
            else:
                sys.stdout.write(c)
        print ('')
    if (ch == 's'):
        os.system('clear')
        y = y - 1
        for i in range (10):
            if i == x:
                sys.stdout.write('@')
            else:
                sys.stdout.write(c)
        print ('')
    if (ch == 'd'):


        os.system('clear')
        x = x + 1
        if (x > 9):
            x = 9

        for i in range (10):
            if i == x:
                sys.stdout.write('@')
            else:
                sys.stdout.write(c)
        print ('')


    if (ch == 'a'):
        os.system('clear')
        x = x - 1
        if (x < 0):
            x = 0

        for i in range (10):
            if i == x:
                sys.stdout.write('@')
            else:
                sys.stdout.write(c)
        print ('')
    #  os.system('clear')
    if (x < 0):
        x = 1
