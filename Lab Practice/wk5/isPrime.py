#################
# Module for Q4 #
#################

def isPrime(a):
    for x in range(2, a):
        if a % x == 0:
            return "not prime"
    return "prime"