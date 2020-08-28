# Noah Cousino
# R01506332

# collect inputs
sub, gratr = eval(input("Input the subtotal and gratuity rate (subtotal, gratuity): "))

# convert percent to decimal
gratr /= 100

# get gratuity
grat = gratr * sub

# display results
print(f"The gratuity is {grat} and the total is {grat + sub}")

# I wasn't sure what the formula actually was so I hope what I did is correct