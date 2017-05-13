#!/usr/bin/python3
from time import sleep
from getch import getch

while (True):
    ch = getch()
    if (ch == 'k'):
        for i in range(4):
            print (ch)
            sleep(1)
    elif (ch == 'q'):
        quit()


# person3 = '''
#  (|)
#   I
#  [#]
#  \/
#  > |
#    <
# '''
