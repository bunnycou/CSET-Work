# imports

# input
filename = input("Enter name of file: ") or "scores.txt"

f = open(filename)

ls = list(f.readlines())

total = 0
for x in ls:
    total += int(x)

average = total/len(ls)

# give outputs
print(f"There are {len(ls)} scores")
print(f"The scores total {total}")
print(f"The scores average {round(average, 2)}")