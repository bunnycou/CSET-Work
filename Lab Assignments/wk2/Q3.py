# import datetime
from datetime import datetime, timedelta

# collect input
off = eval(input("Time zone offset to GMT (such as -5): "))

# get current time in utc same as GMT, calculate time
now = datetime.utcnow()
result = now + timedelta(hours=off)

# display results
print(f"The time is {result}")