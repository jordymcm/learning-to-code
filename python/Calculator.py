#!/usr/bin/python3

n1=0
wh1=0
n2=0
a1=0

n1 = input ('What number?')
n1 = int(n1)

wh1 = input ('Whot do you whont to do whith it?')

n2 = input ('What number?')
n2 = int(n2)

if wh1 == '+':
    print (n1 + n2)

elif wh1 == '-':
    print (n1 - n2)

elif wh1 == '*':
    print (n1 * n2)

elif wh1 == '/':
    print (n1 / n2)

else:
    print ('ples tri agen')
