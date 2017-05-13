#!/usr/bin/python3
#
# Text colors:
#     grey
#     red
#     green
#     yellow
#     blue
#     magenta
#     cyan
#     white
#
# Text highlights:
#     on_grey
#     on_red
#     on_green
#     on_yellow
#     on_blue
#     on_magenta
#     on_cyan
#     on_white
#
# Attributes:
#     bold
#     dark
#     underline
#     blink
#     reverse
#     concealed

from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

words = ['AAA', 'BBB', 'CCC']
pos=2

for index, word in enumerate(words, start=0):
    color = 'red' if (pos == index) else 'white'
    text = colored(word, color)
    print(index, text)
