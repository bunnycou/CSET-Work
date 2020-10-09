# Noah Cousino
# R01506332

# Determine if it is a valid social security number

# collect ssn
ssn = input("Input Social Security Number (ddd-dd-dddd): ")

# evaluate if it is valid based on
# ddd-dd-dddd (11 long)
# check the basic length, check for hyphen
if len(ssn) != 11 or ssn.count('-') < 2:
    print("Invalid SSN")
    exit(0)

# iterate through each character and make sure it is a number or hyphen
for x in ssn:
    if x == '-':
        pass
    elif ord(x) >= 48 and ord(x) <= 57:
        pass
    else:
        print("Invalid SSN")
        exit(0)

# if nothing comes up invalid say it is valid
print("Valid SSN")