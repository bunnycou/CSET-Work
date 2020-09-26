# Noah Cousino
# R01506332

# Test
##############
# Question 1 #
##############
# Convert C to F and F to C

# import module
from FConvert import fToc, cTof

# display results
print("Celsius --> Fahrenheit |   Fahrenheit --> Celsius\n")
#iterator for fahrenheit
f = 120
# x is for the slight adjustment made to the table when fahrenheit switches digit count
x = 0
for c in range(30, 40):
    if f < 100:
        x = 5
    print(f"{format(c, '.1f')}        {format(cTof(c), '.1f')}      |   {format(f, '.1f')}          {format(fToc(f), '.1f').rjust(x)}")
    f -= 10