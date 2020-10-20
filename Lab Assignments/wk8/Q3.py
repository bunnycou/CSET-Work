# Noah Cousino
# R01506332

##############
# Question 3 #
##############

# collect input
numi = input("Enter ten numbers separated by spaces: ")

# a list should probably be used to display the results because that is what this chapter is so I will make a list
# but I will also display the results using a for loop to show the combinations
nums = numi.split()
results = []
result = ""

# find results
for x in range(0, 10):
    for y in range(x+1, 10):
        results.append(eval(nums[x]) + eval(nums[y]))
        result = f"{result}\n{nums[x]} + {nums[y]} = {eval(nums[x]) + eval(nums[y])}"

# display the results
print("The results are...")
for x in range(0, len(results)):
    if x % 15 == 0:
        print("")
    if results[x] < 10:
        print(f" {results[x]}", end=" ")    
    else:
        print(results[x], end=" ")
print(result)