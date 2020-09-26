# Noah Cousino
# R01506332

# import randint
from random import randint

# start loop to do 10 questions
for x in range (0, 10):

    # get random numbers and answers
    a = randint(1, 15)
    b = randint(1, 15)
    ans = a + b
    
    # make larger number come first
    # not necessary for addition problems but I still like to see the larger number first
    if b > a:
        a, b = b, a
    
    # collect the guess
    guess = eval(input(f"{x+1}) {a} + {b} = "))

    # evaluate the guess
    if guess == ans:
        print("   Correct!")
    else:
        print(f"   Wrong! The answer was {ans}")
