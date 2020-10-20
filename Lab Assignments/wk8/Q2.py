# Noah Cousino
# R01506332

##############
# Question 2 #
##############

# create function for finding the smallest element index
def indexOfSmallestElement(nums):
    # store the smallest number and position of it
    mins = [nums[0], 0]
    
    # iterate through all of the numbers
    for x in range(1, len(nums)):
        if nums[x] < mins[0]:
            mins[0] = nums[x]
            mins[1] = x

    return mins[1]


# get input
numi = input("Enter a list of numbers seperated by a space: ")
nums = numi.split()

# evaluate input and find the smallest index
ind = indexOfSmallestElement(nums)

# display the smallest index assuming you use non-programmer index
print(f"The index of the smallest number is at {ind+1}")