##############
# Question 7 #
##############
# returning multiple values

def sort(a, b):
    if a < b:
        return a, b
    else:
        return b, a

x, y = sort(5, 2)
print(f"First number is {x}\nSecond number is {y}")