# DAY 2-3 EXERCISE - LIFE IN WEEKS CALCULATOR
# USING F STRINGS

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
days = (90 * 365) - (age_as_int * 365)
weeks = (90 * 52) - (age_as_int * 52)
months = (90 * 12) - (age_as_int * 12)
print(f"You have {days} days, {weeks} weeks, and {months} months left")

# THE CLEANER WAY TO CODE THIS
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(message)