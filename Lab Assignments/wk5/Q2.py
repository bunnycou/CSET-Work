# Noah Cousino
# R01506332

# Test
##############
# Question 2 #
##############
# Test for Accountant

# import class
from Accountant import Accountant

# make an object
user = Accountant(1122, 20000, 4.5)

# test functions
user.withdraw(2500)
user.deposit(3000)

# display info
print(f"ID: {user.getID()}\nBalance: ${user.getBalance()}\nMonthly Interest Rate: {user.getMonthlyInterestRate()}%\nMonthly Interest: ${user.getMonthlyInterest()}")
