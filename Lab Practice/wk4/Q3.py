############
# Question 3
############
# Display BMI

# collect weight and height
weight = eval(input("How much do you weigh? "))
height = eval(input("How tall are you? "))

# constants for conversion
WKG = 0.45359237
HM = 0.0254

# convert to metrics
kg = weight * WKG
m = height * HM

bmi = kg / m**2

print(f"Your BMI is: {round(bmi, 1)}")