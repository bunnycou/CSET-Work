# Noah Cousino
# R01506332

# variable for counting up and creating new line
x = 0

for i in range(100, 201):
    # evaluate if number fits the conditions
    if i % 5 == 0 and i % 6 == 0:
        pass
    elif i % 5 == 0:
        print(i, end=" ")
        x += 1
    elif i % 6 == 0:
        print(i, end=" ")
        x += 1

    # make a new line if there has been 10 numbers
    if x == 10:
        x = 0
        print("")

    