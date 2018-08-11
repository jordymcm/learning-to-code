#!/usr/bin/python3

from getch import getch
import os

ch = 0
chs = 0
pos = 1
dd = 0
an = 0

while (True):

    if dd == 0:

        os.system('clear')

#
# text = colored('Jordy', 'green', attrs=[])
# print(text)
#
# text = colored('Jordy', 'green', attrs=[])
# print(text)
#
# text = colored('Jordy', 'green', attrs=[])
# print(text)
#
# text = colored('Jordy', 'green', attrs=[])
# print(text)



        words = ['Pavlina', 'Jordan', 'Tim', 'New slot']

        for index, word in enumerate(words, start=0):
            color = 'red' if (pos == index) else 'white'
            text = colored(word, color)
            print(text)

        ch = getch()


        if (ch == 'w'):
            pos = pos - 1

        if (ch == 's'):
            pos = pos + 1

        if (pos == -1):
            pos = 0

        if (pos == len (words)):
            pos = len (words) -1

        #chs = getch()
        #chs = int (ch)
        if (ch == '\n'):

            if (pos == 0):
                os.system('clear')
                print ('eee')
            if (pos == 1):
                os.system('clear')
                print ('Age(')
                print ('9.5 berthday jalay the fith)')

            if (pos == 2):
                print ('hi')
                sleep(1)
            if (pos == 3):
                an = 4
            sleep(1)
