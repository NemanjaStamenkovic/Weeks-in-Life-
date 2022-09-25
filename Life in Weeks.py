print("Welcome To Life In Weeks.")
ageCurrent = int(input(("What is Your Current Age?: ")))

ageLeft = 90 - ageCurrent

weeksLeft = ageLeft * 52
daysLeft = ageLeft * 365
monthsLeft = ageLeft * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} left.")