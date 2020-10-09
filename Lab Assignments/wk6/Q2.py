# Noah Cousino
# R01506332

# check password for requirements

# collect passwrod
pswd = input("Input your password: ")

# evaluate against requirements
# At least 8 characters
# Only letters and numbers
# At least two numbers

# track if there was an error
err = True

# check length
if len(pswd) < 8:
    print("Passwords must be at least 8 characters")
    err = False

# iterate through each character and check if it is a letter or number and count the numbers
nums = 0
pos = 1
for x in pswd:
    if (ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 65 and ord(x) <= 90):
        pass
    elif ord(x) >= 48 and ord(x) <= 57:
        nums += 1
    else:
        print(f"Invalid Character at {pos}: {x}")
        err = False
    pos += 1

# check if there are enough digits
if nums < 2:
    print("Passwords must include at least two numbers")
    err = False

# runs if no problems are found
if err:
    print("Your password is valid")