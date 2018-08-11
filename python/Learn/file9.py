#!/usr/bin/python3

ch = 0

t = '.'
p = '.'
from time import sleep
import os
import sys
from getch import getch
ch = 0
while True:
    p = t

    h = getch()
    if h == 'w':
        if ch < 3:
            ch += 1

    if h == 's':
        if ch > -1:
            ch -= 1

    os.system('clear')

    print('|----------|')
    if (ch == 3):
        p = '@'
    sys.stdout.write('|')
    for i in range (10):
        sys.stdout.write(p)
    print('|')

    p = t


    if (ch == 2):
        p = '@'

    sys.stdout.write('|')
    for i in range (10):
        sys.stdout.write(p)
    print('|')

    p = t


    if (ch == 1):
        p = '@'


    sys.stdout.write('|')
    for i in range (10):
        sys.stdout.write(p)
    print('|')

    p = t

    if (ch == 0):
        p = '@'

    sys.stdout.write('|')
    for i in range (10):
        sys.stdout.write(p)

    print('|')
    p = t

    if (ch == -1):
        p = '@'


    sys.stdout.write('|')
    for i in range (10):
        sys.stdout.write(p)
    print('|')

    p = t

    print('|----------|')
    #sleep(1)
