# constants for conversions
WK = 0.45359237
HM = 0.0254

# collect inputs
w = eval(input("Weight in pounds: "))
h = eval(input("Height in inches: "))

# convert to metrics
k = w * WK
m = h * HM

# calculate bmi
b = k / (m**2)

# print result and round it to the first decimal place for readability
print(f"BMI is {round(b, 1)}")