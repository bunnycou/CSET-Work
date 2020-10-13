##############
# Question 4 #
##############
# Count the occurence of letters

# import method for creating random characters
from randomCharacter import randomLower

# make a list of random characters
chars = []

for x in range(100):
    chars.append(randomLower())

# display all of the characters
for x in range(len(chars)):
    if (x + 1) % 20 == 0:
        print(chars[x])
    else:
        print(chars[x], end = " ")

print("\n---\n")

counts = 26*[0]

for x in range(len(chars)):
    counts[ord(chars[x]) - ord('a')] += 1

for x in  range(len(counts)):
    if (x + 1) % 13 == 0:
        print(counts[x], chr(x + ord('a')))
    else:
        print(counts[x], chr(x+ord('a')), end = ' ')
