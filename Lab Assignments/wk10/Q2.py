# Noah Cousino
# R01506332

# collect input
num = input("Input a single line of numbers: ")

nums = dict()

# create dict of nums
for x in num.strip().split(" "):
    y = int(x)
    if x in nums:
        nums[x] += 1
    else:
        nums[x] = 1

# check for the top nums
high = 0
ans = list()
for x in nums:
    if nums[x] > high:
        high = nums[x]
        ans.clear()
        ans.append(x)
    elif nums[x] == high:
        ans.append(x)

# display results
print(f"The high {'numbers are...' if len(ans) > 1 else 'number is...'}")
for x in ans:
    print(f"{x} appears {nums[x]} {'times' if nums[x] > 1 else 'time'}")
