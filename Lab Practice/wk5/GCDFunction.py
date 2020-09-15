#################
# Module for Q3 #
#################
# find the greatest common divisor

def gcd(a, b):
    gcd = 1 # initial gcd
    k = 2 # potential gcd
    while k <= a and k <= b:
        if a % k == 0 and b % k == 0:
            gcd = k
        k += 1
    return gcd