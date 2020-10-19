# grab the file
f = open("file9.txt", "r")
# set file contents to a list of lines
fls = f.readlines()
# close file now that we have everything
f.close()

# create our list, set, and dict pairs
ls = list()
nls = list()
sett = set()
nsett = set()
dicty = dict()
ndicty = dict()

# iterate through the lines and put everything into a list
for x in fls:
    line = x.split()
    for y in line:
        ls.append(y)

# create the new list with no duplicates
for x in ls:
    if x not in nls:
        nls.append(x)

# display list
print("List:")
for x in nls:
    print(x)

# iterate through the lines and put everything into a set
for x in fls:
    line = x.split()
    for y in line:
        sett.add(y)

# create the new set with no duplicates
for x in sett:
    if x not in nsett:
        nsett.add(x)

# display set
print("\nSet:")
for x in nsett:
    print(x)

# iterate through the lines and put everything into a dict
# why would you do this...
for x in fls:
    line = x.split()
    for y in range(0, len(line)):
        dicty[f"{y}"] = line[y]

# check if something exists in the dictionary
# have a variable to check if it exists in both dicts
contains = False
# this is cancer...
for x in range(0, len(dicty)):
    for y in ndicty:
        if dicty[f"{x}"] == y:
            contains = True
    if not contains:
        print(dicty[f"{x}"])
        ndicty[f"{x}"] = dicty[f"{x}"]

# display dict
print("\nDict:")
for x in ndicty:
    print(x)
