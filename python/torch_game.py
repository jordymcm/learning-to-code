#!/usr/bin/python3

from time import sleep
from getch import getch
import os
cr = getch
Onof = 0
cr = 0
while True:
    os.system('clear')
    if Onof == 0:
        print ('')
        print ('')
        print ('')
        print ('')
        print ('')
        print ('')
        print ('|-------------|')
        print ('|      / \\    |')
        print ('|      \\ /    |')
        print ('|-------------|')
        print ('')
        print ('')
        print ('')
        print ('')
        print ('')
        print ('')
        print ('')
        
    else:
        print ('                    /##')
        print ('                   /###')
        print ('                  /####')
        print ('                 /#####')
        print ('                /######')
        print ('               /#######')
        print ('|-------------|########')
        print ('|     / \\     |########')
        print ('|     \\ /     |########')
        print ('|-------------|########')
        print ('               \\#######')
        print ('                \\######')
        print ('                 \\#####')
        print ('                  \\####')
        print ('                   \\###')
        print ('                    \\##')
        print ('')

    sleep(1)

    if (getch() == 'w'):

        Onof = 1 - Onof
