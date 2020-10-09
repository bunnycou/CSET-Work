# Noah Cousino
# R01506332

# reverse a string

def reverse(s):
    new = ""
    for x in range(1, len(s)+1):
        new += s[-x]
    return new