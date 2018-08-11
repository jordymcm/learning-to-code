#!/usr/bin/python3

number = 0

number2 = 0
number1 = 2010
age = input ('haw olde ar you: ')

age = int (age)

number1 = number1 - age

number = number1 * 3
print (number)

have = input ('have you had a berth day this yier say 1 for yes 2 for no')

if have == 1:
    number = number + 21
    
    print (number)
    
elif have == 2:
    number = number + 20
    
    print (number)
    
number2 = number / 3

# number2 = int (number2)

print ('you wer born in')
print (number2)