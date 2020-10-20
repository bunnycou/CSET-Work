##############
# Question 3 #
##############
# Use 3-D lists that guess the birthday by asking 5 questions

day = 0 # day to be determined

dates = [
    [[1, 3, 5, 7],
    [9, 11, 13, 15],
    [17, 19, 21, 23],
    [25, 27, 29, 31]],
    [[2, 3, 6, 7],
    [10, 11, 14, 15],
    [18, 19, 22, 23],
    [26, 27, 30, 31]],
    [[4, 5, 6, 7],
    [12, 13, 14, 15],
    [20, 21, 22, 23],
    [28, 29, 30, 31]],
    [[8, 9, 10, 11],
    [12, 13, 14, 15],
    [24, 25, 26, 27],
    [28, 29, 30, 31]],
    [[16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31]]
]

for x in range(0, 5):
    print(f"Is your birthday in set {str(x + 1)}?")
    for y in range(0, 4):
        for z in range(0, 4):
            print(format(dates[x][y][z], "4d"), end = " ")
        print()
    answer = eval(input("Enter 0 for No and 1 for Yes: "))

    if answer == 1:
        day += dates[x][0][0]

print(f"Your birthday is {str(day)}")
