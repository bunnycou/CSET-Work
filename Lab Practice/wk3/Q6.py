############
# Question 6
############
print("Question 6 - Max number of dollars and coins with integer")

# get moneys
cents = eval(input("Input amount of as pennies (11.56 as 1156): "))

# get cents, dollars, quarters, dimes, nickels, penies

dollars = cents//100
cents -= dollars*100

quarters = cents//25
cents -= quarters*25

dimes = cents//10
cents -= dimes*10

nickels = cents//5
cents -= nickels*5

pennies = cents

# display money
print(f"\nDollars: {dollars}\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}")