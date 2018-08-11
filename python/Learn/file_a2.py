#!/usr/bin/python3
c = 0
b = 0
a = 0
t = 0
con = 0

import os
from time import sleep
from random import randint
os.system('clear')

level = int(input ('Level 1-3'))
if (level == 1):
    c = 1
    d = 10

if (level == 2):
    c = 10
    d = 150

if (level == 3):
    c = 200
    d = 500
for i in range (3):

    b = randint (c, d)
    a = randint (c, d)
    print (a)
    print ('+')
    print (b)
    con = int(input ('='))

    t = a + b

    if (con == t):

        print ('         /')
        print ('        /')
        print ('\\      /')
        print (' \\    /')
        print ('  \\  /')
        print ('    /')


    else:

        print ('\\   /')
        print (' \\ /')
        print ('   ')
        print (' / \\')
        print ('/   \\')
    sleep(2)
    os.system('clear')


c = 0
b = 0
a = 0
t = 0
con = 0
level = int(input ('Level 1-3'))
if (level == 1):
    c = 1
    d = 10

if (level == 2):
    c = 10
    d = 100

if (level == 3):
    c = 200
    d = 500
for i in range (3):

    b = randint (c, d)
    a = randint (c, d)
    while (a < b or a == 0 or b == 0):
        b = randint (c, d)
        a = randint (c, d)
    print (a)
    print ('-')
    print (b)
    con = int(input ('='))

    t = a - b

    if (con == t):

        print ('         /')
        print ('        /')
        print ('\\      /')
        print (' \\    /')
        print ('  \\  /')
        print ('    /')


    else:

        print ('\\   /')
        print (' \\ /')
        print ('')
        print (' / \\')
        print ('/   \\')
    sleep(2)
    os.system('clear')




c = 0
b = 0
a = 0
t = 0
con = 0
level = int(input ('Level 1-3'))
if (level == 1):
    c = 2
    d = 7

if (level == 2):
    c = 10
    d = 150

if (level == 3):
    c = 200
    d = 500
for i in range (3):

    b = randint (c, d)
    a = randint (c, d)
    print (a)
    print ('X')
    print (b)
    con = int(input ('='))

    t = a * b

    if (con == t):

        print ('         /')
        print ('        /')
        print ('\\      /')
        print (' \\    /')
        print ('  \\  /')
        print ('    /')


    else:

        print ('\\   /')
        print (' \\ /')
        print ('   ')
        print (' / \\')
        print ('/   \\')
    sleep(2)
    os.system('clear')



c = 0
b = 0
a = 0
t = 0
con = 0
level = int(input ('Level 1-3'))
if (level == 1):
    c = 2
    d = 7

if (level == 2):
    c = 10
    d = 100

if (level == 3):
    c = 200
    d = 500
for i in range (3):

    b = randint (c, d)
    a = randint (c, d)
    print (a)
    print (' .')
    print ('---')
    print (' .')
    print (b)
    con = int(input ('='))

    t = a / b

    if (con == t):

        print ('         /')
        print ('        /')
        print ('\\      /')
        print (' \\    /')
        print ('  \\  /')
        print ('    /')


    else:

        print ('\\   /')
        print (' \\ /')
        print ('   ')
        print (' / \\')
        print ('/   \\')
    sleep(2)
    os.system('clear')
