##############
# Question 8 #
##############
# generate random characters

import randomCharacter

NUMBER_OF_CHARS = 175
CHAR_PER_LINE = 25

# print a lot of characters
for x in range(NUMBER_OF_CHARS):
    print(randomCharacter.randomLower(), end = " ")
    if (x + 1) % CHAR_PER_LINE == 0:
        print()

