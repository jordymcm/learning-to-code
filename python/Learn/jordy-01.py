#!/usr/bin/python3


import os
from time import sleep

def right ():
    print ('you cros a brig and you see sumthing in t going acros the')

os.system('clear')

print ('welcome to Jordys adventure game')
sleep (2)
os.system('clear')

print ('How dow you wont to be ?')

who = input ('1-a rock klimer 2-a sprint runer 3-a gamer: ')

who = int (who)

if who == 1:
    print ('you chos a rock klimer')
else:
    if who == 2:
        print ('you chos a sprint runer')
    else:
        if who == 3:
            print ('you chos a gamer')
            
sleep (4)
os.system('clear')

print ('you see a parth you cane')
go = input ('1-go fowad: ')
go = 0
os.system('clear')
print ('you came up to an intosacshon you can')
go = input ('1-go right 2-go left: ')
go = int (go)
if go == 1:

