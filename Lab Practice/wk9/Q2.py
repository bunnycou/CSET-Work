##############
# Question 2 #
##############
# Deck of Cards: Display 4 cards from the deck of 52

# create a deck of cards
deck = [x for x in range(52)]

# create suit and ranks
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["Aces", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

from random import shuffle

shuffle(deck)

for x in range(4):
    suit = suits[deck[x]//13]
    rank = ranks[deck[x]%13]
    print(f"Card Number {deck[x]} is the {rank} of {suit}")