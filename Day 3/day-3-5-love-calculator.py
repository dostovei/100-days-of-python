# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# lowercase_name1 = name1.lower()
# lowercase_name2 = name2.lower()
# lowercase_names = lowercase_name1 + lowercase_name2

# true = lowercase_names.count("t") + lowercase_names.count("r") + lowercase_names.count("u") + lowercase_names.count("e")

# love = lowercase_names.count("l") + lowercase_names.count("o") + lowercase_names.count("v") + lowercase_names.count("e")

# love_score = int(str(true) + str(love))

# if love_score <= 10 or love_score >= 90:
#   print(f"Your score is {love_score}, you go together like diet coke and mentos.")
# elif love_score > 40 and love_score < 50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")

# SOLUTION HOW IT'S CODED BY ANGELA BELOW
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like diet coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")