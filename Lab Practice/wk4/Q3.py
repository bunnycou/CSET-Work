############
# Question 3
############
# Display BMI

# collect weight and height
weight = eval(input("How much do you weigh in pounds? "))
height = eval(input("How tall are you in inches? "))

# constants for conversion
WKG = 0.45359237
HM = 0.0254

# convert to metrics
kg = weight * WKG
m = height * HM

bmi = kg / m**2

print(f"Your BMI is: {round(bmi, 1)}")
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are at a normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")