# DAY 1 - 100 DAYS OF PYTHON

# name = "Jack"
# print(name)

# name = "Sam"
# print(name)


name = input("What is your name?")
length = len(name)
print(length)

# VARIABLE NAMING
# 1. user_name >>> two words must be separated with an underscore
# 2. cannot have a number at the beginning of variable name
# 3. input = input >>> using the same name for your variable as the function
# 4. NameError example: name =/= nama, watch for typos

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c
#COMMON CODE INTERVIEW QUESTION

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)