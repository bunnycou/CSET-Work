##############
# Question 1 #
##############
# Lotto Numbers: Reading files

# create a list of 99 boolean elements that are false
isCovered = 99 * [False]
endOfInput = False
while not endOfInput:
    # read numbers as string from the consolle
    s = input("Enter a line of numbers seperated by spaces: ")
    items = s.split()
    lst = [eval(x) for x in items]

    # check the numbers
    for number in lst:
        if number == 0:
            endOfInput = True
        else:
            isCovered[number-1] = True

# check if all numbers are covered
allCovered = True
for x in range(99):
    if not isCovered[x]:
        allCovered = False
        break

# display result
if allCovered:
    print("The ticket covers all numbers")
else:
    print("The tickets don't cover all numbers")