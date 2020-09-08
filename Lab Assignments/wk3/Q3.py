# Noah Cousino
# R01506332

# import random
import random

# create a list of the available choices
choices = ["rock", "paper", "scissors"]

choice = choices[eval(input("Rock (0), Paper (1), Scissors(2): "))]
pc = choices[random.randint(0, 2)]

# set of if statements to determine who wins
if (choice == "rock" and pc == "scissors") or (choice == "paper" and pc == "rock") or (choice == "scissors" and pc == "paper"):
    print(f"Player threw {choice}\nComputer threw {pc}\nPlayer Wins!")
elif (pc == "rock" and choice == "scissors") or (pc == "paper" and choice == "rock") or (pc == "scissors" and choice == "paper"):
    print(f"Player threw {choice}\nComputer threw {pc}\nComputer Wins!")
else:
    print(f"Both players threw {choice}\nIt's a tie!")
