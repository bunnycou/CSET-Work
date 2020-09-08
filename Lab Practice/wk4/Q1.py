############
# Question 1
############
# Find out date of birth from five questions

day = 0

# collect all of the answers to the five sets
first = input("""Is your birthday one of these numbers?
                 1  3  5  7
                 9 11 13 15
                17 19 21 23
                25 27 29 31
                (Y/N): """)[0].lower()

second = input("""\nIs your birthday one of these numbers?
                 2  3  5  7
                10 11 14 15
                18 19 22 23
                26 27 30 31
                (Y/N): """)[0].lower()

third = input("""\nIs your birthday one of these numbers?
                 4  5  6  7
                12 13 14 15
                20 21 22 23
                28 29 30 31
                (Y/N): """)[0].lower()

fourth = input("""\nIs your birthday one of these numbers?
                 8  9 10 11
                12 13 14 15
                24 25 26 27
                28 29 30 31
                (Y/N): """)[0].lower()

fifth = input("""\nIs your birthday one of these numbers?
                16 17 18 19
                20 21 22 23
                24 25 26 27
                28 29 30 31
                (Y/N): """)[0].lower()

# evaluate if their number was in the set and add the required number to the day
if first == "y":
    day += 1
if second == "y":
    day += 2
if third == "y":
    day += 4
if fourth == "y":
    day += 8
if fifth == "y":
    day += 16

# display the day
print(f"\n\nYour birth day is {day}")