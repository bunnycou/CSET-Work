##############
# Question 1 #
##############
# function practice of finding the max number
def max(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    i = 11
    j = 7
    k = max(i, j)
    print(f"The largest of {i} and {j} is {k}")

main()