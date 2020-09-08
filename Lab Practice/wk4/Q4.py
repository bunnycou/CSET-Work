############
# Question 4
############
#Lottery Machine
# 2 Digit lotto number
# If guess is correct get 10k
# if both numbers are guessed in wrong order get 3k
# if one number is guessed get 1k

# import the random int
from random import randint

# get the magic number, coded this way to make 00 - 09 a possibility
lottoa = f"{randint(0,9)}"
lottob = f"{randint(0,9)}"
lotto = f"{lottoa}{lottob}"

# have this for testing purposes
# print (f"Lotto number is {lotto}")

# get the guess
guess = input("What is your guess? ")
guessa = guess[0]
guessb = guess[1]

#create a spacer
print("\n")

# evaluate guess against lotto number
if guess == lotto:
    print(f"You've guessed the number and won $10,000!\nLottery Number: {lotto}\nGuess: {guess}")
elif guessa == lottob and guessb == lottoa:
    print(f"You've gussed both numbers in reverse order and won $3,000!\nLottery Number: {lotto}\nGuess: {guess}")
elif guessa == lottoa or guessa == lottob or guessb == lottoa or guessb == lottob:
    print(f"You've guessed one of the numbers and won $1,000!\nLottery Number: {lotto}\nGuess: {guess}")
else:
    print(f"Sorry! You gussed wrong and didn't win anything!\nLottery Number: {lotto}\nGuess: {guess}")