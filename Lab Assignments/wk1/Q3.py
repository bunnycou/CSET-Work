# Noah Cousino
# R01506332

# Store information in variables
dist = 14 #km
time = 45.5 #min
# find our miles and hour
mi = dist/1.6
hr = time/60
# calculate mph
mph = mi/hr

# display result using f string
print(f'{mph} mph')

# displays result rounded to the tenths place
print(f'{round(mph, 1)} mph')