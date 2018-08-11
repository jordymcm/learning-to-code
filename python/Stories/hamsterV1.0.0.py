#!/usr/bin/python3

from getch import getch
import os

answer=0
name=0

answer = input ('You are a hamster what\'s your name? A: Fred B: doggy C: Zoof ')

os.system('clear')

if answer == 'a' or answer == 'A':
    name=('fred')
    print ('Fred, that is a good choice')
    getch() == ' '
    os.system('clear')
    answer = input ('Now '+ name +' needs a house. you have 2 choises. A: a house B: a flata ')
    
elif answer == 'b' or answer == 'B':
    name=('doggy')
    print ('doggy, that is a good choice')
    getch() == ' '
    os.system('clear')
    answer = input ('Now '+ name +' needs a house. you have 2 choises. A: a house B: a flata ')
    
elif answer == 'c' or answer == 'C':
    name=('zoof')
    print ('zoof, that is a good choice')
    getch() == ' '
    os.system('clear')
    answer = input ('Now '+ name +' needs a house. you have 2 choises. A: a house B: a flata ')