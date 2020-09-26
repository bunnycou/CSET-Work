# Noah Cousino
# R01506332

# Module 
##############
# Question 2 #
##############
# Class for Accountant

# create class
class Accountant:
    # set variables
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate / 100

    # fet monthly rate
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    # get monthly interest
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    # withdraw money
    def withdraw(self, amount):
        self.__balance -= amount

    # deposit money
    def deposit(self, amount):
        self.__balance += amount

    # print the id
    def getID(self):
        return self.__id
    
    # print the balance
    def getBalance(self):
        return self.__balance
    
    # print the intereest rates
    def getAnnualInterest(self):
        return self.__annualInterestRate