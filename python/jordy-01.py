#!/usr/bin/python3

from time import sleep
print ('welcome to Jordys adventure game')
# sleep (2)
print ('How dow you wont to be ?')
who = input ('1-a rock klimer 2-a sprint runer 3-a gamer')

who = int (who)

if who == 1:
    print ('you chos rock klimer')
else:
    if who == 2:
        print ('you chos sprint runer')
    else:
        if who == 3:
            print ('you chos gamer')