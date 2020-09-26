# Noah Cousino
# R01506332

# create variable to find the largest number
n = 0

# iterate through every number up through the cubic root of 12000
while n < (12000 ** (1/3) // 1):
    if n ** 3 > 12000:
        break
    else:
        n += 1
# display result
print(f"{n} is the largest number meeting the conditions")