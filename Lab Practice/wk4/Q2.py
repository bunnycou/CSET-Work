############
# Question 2
############
# randomly generate subtraction problem and evaluate if answer is right or wrong

# import random
from random import randint

# get two random numbers between 0 and 100 and get the answer
a = randint(0, 9)
b = randint(0, 9)

# swap numbers so that there are no negatives
if a < b:
    a, b = b, a

ans = a - b

# collect guess
guess = eval(input(f"{a} - {b} = "))

# evaluate guess
if guess == ans:
    print(f"Correct! The answer was {ans}")
else:
    print(f"Sorry that was incorrect.\nYou guessed {guess}\nThe answer was {ans}")
