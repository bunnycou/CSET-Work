# Noah Cousino
# R01506332

##############
# Question 1 #
##############

# collect input
numin = input("Enter ten numbers seperated by a space: ")

# split the input into a list
nums = numin.split()

# create a list for the unique numbers
unums = []

# check if the number exists in the list or not
for x in nums:
    if x not in unums:
        unums.append(x)

# create a string for the unique numbers
unus = " "
unus = unus.join(unums)

# display the unique numbers
print(f"The distinc numbers are: {unus}")