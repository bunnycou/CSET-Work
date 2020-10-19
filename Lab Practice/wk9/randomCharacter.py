#################
# Module for Q8 #
#################

from random import randint

def randomChar(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

def randomLower():
    return randomChar('a', 'z')

def randomUpper():
    return randomChar('A', 'Z')

def randomDigit():
    return randomChar('0', '9')

def randomASCII():
    return chr(randint(0, 127))
