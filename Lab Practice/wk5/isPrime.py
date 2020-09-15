#################
# Module for Q4 #
#################

def isPrime(a):
    for x in range(2, a//2):
        if a % x == 0:
            return False
    return True

def primes(a, b):
    primeli = ""
    if a > b:
        a, b = b, a
    for x in range(a, b):
        if isPrime(x):
            primeli += f"{x}, "
    primeli = primeli[:-2]
    return primeli