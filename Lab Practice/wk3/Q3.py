############
# Question 3
############
print("Question 3 - Max number of dollars and coins")

# get moneys
amount = eval(input("Input amount of money with decimals (11.56): "))

# get cents, dollars, quarters, dimes, nickels, penies
cents = amount * 100

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