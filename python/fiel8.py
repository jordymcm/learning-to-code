#!/usr/bin/python3

#Ghost Game
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('Three doors ahead')
    print('A ghost behind one')
    print('Which door do you open')
    door = input ('1, 2, or 3: ')
    door_nub = int(door)
    if door_nub == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('No ghost!')
        print('You enter the next room')
        score += 1
print('Run away')
print('Game over! Yor score ', score)
